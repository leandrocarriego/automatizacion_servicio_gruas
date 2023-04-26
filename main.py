import threading
from classes.Driver.Driver import *
from classes.Window import *

class App() :
        def __init__(self):
                self.window = Window() 
                self.driver = Driver()
               
        def start(self) :
                driver_thread = threading.Thread(
                        name='start_driver', 
                        target=self.driver.start_driver,
                        )
                
                self.window.start_window(driver_thread, self.stop )

        def stop(self) :
                self.driver.stop_driver()
                self.window.stop_window()
                
                
app = App()
     
app.start()


