from time import sleep
class ProductDetail():
    def __init__(self,driver):
        self.driver=driver

    def addProductToFavorites(self):
        self.driver.find_element_by_id("getWishList").click()
        sleep(2)
        self.driver.find_element_by_id("addToFavouriteWishListBtn").click()
