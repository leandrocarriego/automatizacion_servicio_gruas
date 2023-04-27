from selenium.webdriver.common.by import By
import time

class Select() :
    def __init__(self, driver) :
        self.driver = driver
        self.xpath = '/html/body/ui-view/div/div/div/div/ui-view/section/div/div[1]/div[2]/uib-accordion/div/div[1]/div[1]/h4/a'
        self.ciclo = True
        
    def setWhile(self) :
        self.ciclo = False
    
    def click(self) :
        item = self.driver.find_element(by=By.XPATH, value=self.xpath)
        while self.ciclo :
            item.click()
            time.sleep(2)
        
