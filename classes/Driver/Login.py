from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from core.config import user, password

class Login() :
    def __init__(self, driver, state_text) :
        self.driver = driver
        self.state_text = state_text

    def login(self) :
        self.state_text('Iniciando sesión...')
        input_user = self.driver.find_element(by=By.NAME, value="username")
        input_password = self.driver.find_element(by=By.NAME, value="password")
        input_user.send_keys(user)
        input_password.send_keys(password)
        input_password.send_keys(Keys.ENTER)
        
            
