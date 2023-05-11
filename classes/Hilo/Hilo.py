import threading
from classes.Driver.Driver import *
import time

class Hilo() :
    def __init__(self, state_text) :
        self.thread = ""
        self.driver = ""  
        self.state_text = state_text
    
    def start(self) :
        self.state_text('Iniciando nueva búsqueda...')
        self.thread = threading.Thread(target=self.thread_action)
        self.thread.start()
    
    def thread_action(self) :
        self.driver = Driver(self.state_text)
        self.driver.start_driver()
        
    def stop(self) :
        self.state_text('Finalizando busqueda...')
        
        if self.driver == "" :
             pass
        else :   
            self.driver.stop_driver()
            self.driver = ""      

        self.thread = ""
        if self.driver == "" and self.thread == "" :
            self.state_text('Búsqueda finalizada')
        
    def restart(self) :
        self.stop()
        time.sleep(3)
        self.start()
        
       