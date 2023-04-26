from selenium import webdriver
from classes.Driver.Login import *

class Driver() :
    def __init__(self) :
        self.driver = webdriver.Chrome(executable_path="../../resources/webDriver/chromedriver.exe")
        self.start_login = Login(self.driver)
        
    def start_driver(self):
        self.driver.get("https://morfeoasistencias.com/#/login")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
        self.start_login.login()
                                    
    def stop_driver(self):
        self.start_login.setWhile()
        self.driver.quit()
    
    