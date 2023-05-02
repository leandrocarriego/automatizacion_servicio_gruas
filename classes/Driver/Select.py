from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Select():
    def __init__(self, driver):
        self.driver = driver
        self.ciclo = True

    def setWhile(self) :
        self.ciclo = False
    
    def buscar_servicios(self):
        while self.ciclo:
            try:
                print("buscando nuevo servicio")
                # element = WebDriverWait(self.driver, 1).until(
                #     EC.presence_of_element_located((By.CLASS_NAME, "btn btn-primary service-btn"))
                # )
                
                element = self.driver.find_element(by=By.CLASS_NAME, value="btn btn-primary service-btn")
                print("se encontro el boton de nuevo servicio")
                element.click()
                print("se hizo click")

                btn_aceptar_servicio = self.driver.find_element(By.XPATH, "//button[text()= 'Aceptar Servicio']")
                print("se encontro el boton aceptar servicio")

                btn_aceptar_servicio.click()
                print("se acepto el sercivio")
                time.sleep(3)
                self.driver.get_screenshot_as_file("screenshot.png")
                
            except :
                pass
                
                

    