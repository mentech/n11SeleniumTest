class MyAccount():
    def __init__(self,driver):
        self.driver=driver
        self.myAccountId="myAccount"
        self.deleteBtnClassName="deleteProFromFavorites"
        self.accountContentClassName="accContent"

    def checkAccountPage(self):
        if "https://www.n11.com/hesabim" not in str(self.driver.current_url):
            self.driver.get("https://www.n11.com/hesabim")

    def gotoMyWishList(self):
        self.checkAccountPage()
        self.driver.find_element_by_id(self.myAccountId).find_element_by_tag_name("ul").find_element_by_link_text("İstek Listelerim").click()
        self.driver.find_element_by_id(self.myAccountId).find_element_by_class_name("listItemWrap").find_element_by_tag_name("a").click()

    def deleteProductFromFavorites(self):
        self.driver.find_element_by_class_name(self.accountContentClassName).find_element_by_class_name(self.deleteBtnClassName).click()


