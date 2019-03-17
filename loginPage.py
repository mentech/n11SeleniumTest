class Login():
    def __init__(self,driver):
        self.driver=driver
        self.emailId="email"
        self.passwordId="password"
        self.loginButtonId="loginButton"

    def clearLoginForm(self):
        driver=self.driver
        driver.find_element_by_id(self.emailId).clear()
        driver.find_element_by_id(self.passwordId).clear()

    def fillLoginForm(self,email,password):
        driver=self.driver
        if "https://www.n11.com/giris-yap" not in str(driver.current_url):
            driver.get("https://www.n11.com/giris-yap")
        self.clearLoginForm()

        driver.find_element_by_id(self.emailId).send_keys(email)
        driver.find_element_by_id(self.passwordId).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element_by_id(self.loginButtonId).click()
