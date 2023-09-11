import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service

from core.config import url
from classes.Driver.Login import *
from classes.Driver.Search import *


class Driver() :
    def __init__(self, state_text: callable) -> None:
        self.service = Service()
        self.options = ChromeOptions()
        self.driver = Chrome(service=self.service, options=self.options)
        self.state_text = state_text
        
        self.driver.get(url)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

        Login(self.driver, self.state_text)

        time.sleep(5)
        
        self.search_services = Search(self.driver, self.state_text)
                    
    def stop_driver(self) -> None:
        self.search_services.stop_search()
        self.driver.quit()
        
        
    
    