
from selenium.webdriver.support.ui import Select
class Register():
    def __init__(self,driver):
        self.driver=driver
        self.firstNameId="firstName"
        self.lastNameId="lastName"
        self.emailId="registrationEmail"
        self.passwordId="registrationPassword"
        self.passwordAgainId="passwordAgain"
        self.genderMaleXpath="//label[@for='genderMale']"
        self.genderFemaleXpath="//label[@for='genderFemale']"
        self.birthDayId="birthDay"
        self.birthMonthId="birthMonth"
        self.birthYearId="birthYear"
        self.acceptContactXpath="//label[@for='acceptContract']"
        self.acceptPromotionMailAndSmsXpath="//label[@for='sendPromotionalMailAndSms']"
        self.submitButtonId="submitButton"

    def clearRegisterForm(self):
        driver=self.driver
        driver.find_element_by_id(self.firstNameId).clear()
        driver.find_element_by_id(self.lastNameId).clear()
        driver.find_element_by_id(self.emailId).clear()
        driver.find_element_by_id(self.passwordId).clear()
        driver.find_element_by_id(self.passwordAgainId).clear()
    
    def fillRegisterForm(self,name,lastname,email,password,isMale=True,birthDay=1,birthMonth=1,birthYear=1990,getPromotion=True):
        driver=self.driver
        if "https://www.n11.com/uye-ol" not in str(driver.current_url):
            driver.get("https://www.n11.com/uye-ol")
        self.clearRegisterForm()

        driver.find_element_by_id(self.firstNameId).send_keys(name)
        driver.find_element_by_id(self.lastNameId).send_keys(lastname)
        driver.find_element_by_id(self.emailId).send_keys(email)
        driver.find_element_by_id(self.passwordId).send_keys(password)
        driver.find_element_by_id(self.passwordAgainId).send_keys(password)

        if isMale:
            driver.find_element_by_xpath(self.genderMaleXpath).click()
        else:
            driver.find_element_by_xpath(self.genderFemaleXpath).click()
        Select(driver.find_element_by_id(self.birthDayId)).select_by_index(birthDay)
        Select(driver.find_element_by_id(self.birthMonthId)).select_by_index(birthMonth)
        Select(driver.find_element_by_id(self.birthYearId)).select_by_visible_text(str(birthYear))

        driver.find_element_by_xpath(self.acceptContactXpath).click()
        if getPromotion:
            driver.find_element_by_xpath(self.acceptPromotionMailAndSmsXpath).click()
    def clickSubmitButton(self):
        self.driver.find_element_by_id(self.submitButtonId).click()
        
    
    def isThereCaptcha(self):
        captchaImage=self.driver.find_elements_by_id("captchaImage")
        for item in captchaImage:
            return True
        return False


