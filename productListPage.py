#from keytorc import searchKey
from time import sleep
class ProductList():
    def __init__(self,driver):
        self.driver=driver

    def checkSearchResult(self,searchKey,keyCountInResult=3):# eğer listelenen sonuçlar içerisinde en az 3 tane samsung texti varsa sonuçlar doğru listelenmiş kabul edilir
        
        searchResultTitleList= self.driver.find_element_by_id("view").find_elements_by_class_name("productName")
        resultsNumber=0
        for item in searchResultTitleList:
            if searchKey.capitalize() or searchKey.upper() or searchKey.lower() in item.text:
                resultsNumber+=1
            if resultsNumber>=keyCountInResult:
                return True
        if resultsNumber<keyCountInResult:
            return False
    
    def gotoListPage(self,listPageNo,searchKey):
        try:
            pages= driver.find_element_by_class_name("pagination").find_elements_by_tag_name("a")
            pages[listPageNo-1].click()
            print("hata")
        except:
            self.driver.get("https://www.n11.com/arama?q="+searchKey+"&pg="+str(listPageNo))

    def clickProductInResultList(self,listNo):
        resultList= self.driver.find_element_by_id("view").find_element_by_tag_name("ul").find_elements_by_class_name("pro")
        resultList[listNo-1].find_element_by_tag_name("a").click()
        sleep(2)


