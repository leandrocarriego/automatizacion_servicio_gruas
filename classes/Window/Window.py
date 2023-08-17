import tkinter as tk
from tkinter import ttk 
from classes.Hilo.Hilo import *

class Window() :
    def __init__(self) :
        self.window = tk.Tk()
        self.thread = Hilo(self.set_state_app)
        self.text_var = tk.StringVar()
        
    def start_window(self) :
        # Window
        self.window.title('Buscador de servicios')
        self.window.geometry('550x270')
        
        # Frames
        title_frame = ttk.Frame(self.window, width= 300, height= 70)
        title_frame.pack_propagate(False)
        title_frame.pack(expand= True)
        
        buttons_frame = ttk.Frame(self.window, width= 300, height= 50)
        buttons_frame.pack_propagate(False)
        buttons_frame.pack(expand= True)
        
        state_frame = ttk.Frame(self.window, width= 400, height= 80)
        state_frame.pack_propagate(False)
        state_frame.pack(expand= True)
        
        autor_frame = ttk.Frame(self.window, width= 200, height= 50)
        autor_frame.pack_propagate(False)
        autor_frame.pack(expand= True)
        
        # Widgets
        title_label = ttk.Label(master= title_frame, text= 'Buscador de servicios', font= ('Arial', 15) )
        start_button = ttk.Button(master= buttons_frame, text= 'Iniciar', command= self.thread.start)
        restart_button = ttk.Button(master= buttons_frame, text= 'Reiniciar', command= self.thread.restart)
        stop_button = ttk.Button(master= buttons_frame, text= 'Finalizar', command= self.stop_window)
        state_label = ttk.Label(master= state_frame, text= '', textvariable= self.text_var)
        
        title_label.pack(expand= True, fill= 'y')
        start_button.pack(side= 'left', expand= True)
        restart_button.pack(side= 'left', expand= True)
        stop_button.pack(side= 'left', expand= True)
        state_label.pack(expand= True)
        
        self.window.mainloop()
    
    def set_state_app(self, text) :
        self.text_var.set(text)
                
    def stop_window(self) :
        self.thread.stop()
        