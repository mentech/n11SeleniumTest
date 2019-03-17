from time import sleep
class Homepage():
    def __init__(self,driver):
        self.driver=driver
        self.registerButtonClassName="btnSignUp"
        self.searchBoxId="searchData"
        self.searchBtnClassName="searchBtn"
        self.myAccountLinkText="Hesabım"
        self.headerId="header"

    def searchProduct(self,searchKey):
        driver=self.driver
        driver.find_element_by_id(self.searchBoxId).clear()
        driver.find_element_by_id(self.searchBoxId).send_keys(searchKey)
        driver.find_element_by_class_name(self.searchBtnClassName).click()
        sleep(3)

    def gotoRegisterPage(self):
        self.driver.find_element_by_class_name(self.registerButtonClassName).click()
    
    def gotoMyAccount(self):
        self.driver.find_element_by_id(self.headerId).find_element_by_link_text(self.myAccountLinkText).click()
        
