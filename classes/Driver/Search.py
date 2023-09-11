import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Search():
    def __init__(self, driver, state_text) -> None:
        self.driver = driver
        self.search = True
        self.state_text = state_text
        
        while self.search:
            try:
                self.state_text('Buscando nuevo servicio...')
                element = WebDriverWait(self.driver, 9000000).until(
                    EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'service-btn')]"))
                )
                self.state_text('Se encontró un nuevo servicio, debe reiniciar la busqueda')
                time.sleep(5)
                self.search = False
            except :
                pass
                
    def stop_search(self) -> None:
        self.search = False

    