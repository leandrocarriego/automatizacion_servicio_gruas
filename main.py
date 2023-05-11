from classes.Window.Window import *

class App() :
        def __init__(self):
                self.window = Window() 
               
        def start(self) :
                self.window.start_window()  
                
                
app = App()
     
app.start()


