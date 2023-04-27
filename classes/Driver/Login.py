from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Login() :
    def __init__(self, driver) :
        self.driver = driver

    def login(self) :
        input_user = self.driver.find_element(by=By.NAME, value="username")
        input_password = self.driver.find_element(by=By.NAME, value="password")
        input_user.send_keys("GRUASCHARLY1")
        input_password.send_keys("charly099")
        input_password.send_keys(Keys.ENTER)
        
            
