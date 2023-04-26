from tkinter import * 

class Window() :
    def __init__(self ) :
        self.window = Tk()
        
        # self.start_driver_button = Button(self.window, text="Iniciar", command=handle_start_driver)
        
    def start_window(self, handle_start, handle_stop) :
        start_driver_button = Button(self.window, text="Iniciar", command=handle_start.start)
        stop_button = Button(self.window, text="Cerrar", command=handle_stop)
        
        self.window.geometry("200x200")
        stop_button.place(x=100, y=100)
        start_driver_button.place(x=110, y=120)
        
        self.window.mainloop()
        
                
    def stop_window(self) :
        self.window.destroy()
        