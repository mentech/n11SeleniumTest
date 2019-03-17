from selenium import webdriver
from time import sleep
import string,random
import homePage, registerPage,productListPage,productDetailPage,myAccountPage,loginPage
import unittest
from selenium.webdriver.support.ui import WebDriverWait

driverChrome=webdriver.Chrome()
homepage=homePage.Homepage(driverChrome)

searchKey="samsung"
def generateRandomMail():
    mail= ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5,15)))
    mailList=["@gmail.com","@hotmail.com","@yahoo.com","@yandex.com"]
    mail=mail+random.choice(mailList)
    return mail

def generateRandomString():
    name= ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5,15)))
    return name

def registerRandomUser(driver=driverChrome):
    homePage.Homepage(driver).gotoRegisterPage()
    registerForm=registerPage.Register(driver)
    registerForm.fillRegisterForm(generateRandomString(),generateRandomString(),generateRandomMail(),"Deneme12345")
    registerForm.clickSubmitButton()
    if registerForm.isThereCaptcha:
        loginUser()
    
def loadHomepage(driver=driverChrome):
    driver.get("https://www.n11.com")
    if "Alışverişin Uğurlu Adresi" in driver.title:
        print("Home page loaded successfully")
    else:
        print("error: homepage was not loaded")
 
def loginUser():
    login=loginPage.Login(driverChrome)
    login.fillLoginForm("oktay_ment@hotmail.com","crPbZ8YxA3N8fyd")
    login.clickLoginButton()
productName=""

#test scenario
class test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=driverChrome
    
    def test_1homepage(self):
        loadHomepage()

    def test_2register_user(self):
        try:
            registerRandomUser()
        except:
            loginUser()

    def test_3search(self):
        homepage.searchProduct(searchKey)
    
    def test_4check_search(self):
        listPage= productListPage.ProductList(driverChrome)
        if listPage.checkSearchResult(searchKey):
            print("search results is correct")
        else:
            print("it seems a problem for results")

    def test_5goto_page(self):
        listPage= productListPage.ProductList(driverChrome)
        listPage.gotoListPage(2,searchKey)
        if "pg=2" in str(driverChrome.current_url):#eğer 2. sayfadaysa url içinde pg=2 vardır
            print("you are in 2. result page")
        
    def test_6add_to_favorites(self):
        listPage= productListPage.ProductList(driverChrome)
        listPage.clickProductInResultList(3)
        productName = driverChrome.find_element_by_class_name("proName").text
        productDetail=productDetailPage.ProductDetail(driverChrome)
        productDetail.addProductToFavorites()

    def test_7wishlist(self):
        account=myAccountPage.MyAccount(driverChrome)
        account.gotoMyWishList()

    def test_8check_in_favorites(self):
        if productName== driverChrome.find_element_by_id("view").find_element_by_class_name("productName").text:
            print("product is in the favorites")

    def test_9delete_favorite(self):
        account=myAccountPage.MyAccount(driverChrome)
        account.deleteProductFromFavorites()
        driverChrome.refresh()
    
    def test_check_notin_favorites(self):
        isProductDeleted=True
        favoriteList=driverChrome.find_element_by_class_name("accContent").find_elements_by_class_name("productName")
        for item in favoriteList:
            if item.text==productName:
                isProductDeleted=False
                break

        if isProductDeleted:
            print("product successfully deleted from favorites")
        else:
            print("error: product is not deleted")

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
