from selenium import webdriver
from classes.Driver.Login import *
from classes.Driver.Select import *
import time

class Driver() :
    def __init__(self) :
        self.driver = webdriver.Chrome(executable_path="../../resources/webDriver/chromedriver.exe")
        self.start_login = Login(self.driver)
        self.click_element = Select(self.driver)
        
    def start_driver(self):
        self.driver.get("https://morfeoasistencias.com/#/login")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

        self.start_login.login()
        time.sleep(5)
        self.click_element.buscar_servicios()
                                    
    def stop_driver(self):
        self.click_element.setWhile()
        self.driver.quit()
    
    