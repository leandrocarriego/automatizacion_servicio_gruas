from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Select():
    def __init__(self, driver):
        self.driver = driver
        self.ciclo = True

    def setWhile(self) :
        self.ciclo = False
    
    def buscar_servicios(self):
        while self.ciclo:
            try:
                element = WebDriverWait(self.driver, 43200).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "btn btn-primary service-btn"))
                )
                element.click()
                
                btn_aceptar_servicio = self.driver.find_element(By.XPATH, "//button[text()= 'Aceptar Servicio']")
                btn_aceptar_servicio.click()
            except:
                pass

    