from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from classes.Driver.Login import *
from classes.Driver.Search import *
import time

class Driver() :
    def __init__(self, state_text) :
        self.options = webdriver.ChromeOptions().add_experimental_option('excludeSwitches', ['enable-logging'])
        self.service = Service('../../resources/driver/chromedriver') 
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.state_text = state_text
        self.start_login = Login(self.driver, self.state_text)
        self.search_services = Search(self.driver, self.state_text)
        
               
    def start_driver(self):
        self.driver.get("https://morfeoasistencias.com/#/login")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.start_login.login()
        time.sleep(5)
            
        self.search_services.start_search()
                    
    def stop_driver(self):
        self.search_services.stop_search()
        self.driver.quit()
        
        
    
    