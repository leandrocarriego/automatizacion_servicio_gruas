from tkinter import Tk, StringVar
from tkinter.ttk import Frame, Label, Button

from Hilo.Hilo import *


class Window:
    def __init__(self) -> None:
        self.window = Tk()
        self.thread = Hilo(self.set_state_app)
        self.text_var = StringVar()
        self.window.title("Buscador de servicios")
        self.window.geometry("550x270")

        # Frames
        title_frame = Frame(self.window, width=300, height=70)

        buttons_frame = Frame(self.window, width=300, height=50)

        state_frame = Frame(self.window, width=400, height=80)

        autor_frame = Frame(self.window, width=200, height=50)

        # Widgets
        title_label = Label(
            master=title_frame, text="Buscador de servicios", font=("Arial", 15)
        )
        start_button = Button(
            master=buttons_frame, text="Iniciar", command=self.thread.start
        )
        restart_button = Button(
            master=buttons_frame, text="Reiniciar", command=self.thread.restart
        )
        stop_button = Button(
            master=buttons_frame, text="Finalizar", command=self.stop_window
        )
        state_label = Label(master=state_frame, text="", textvariable=self.text_var)

        # UI
        title_frame.pack_propagate(False)
        title_frame.pack(expand=True)

        buttons_frame.pack_propagate(False)
        buttons_frame.pack(expand=True)

        state_frame.pack_propagate(False)
        state_frame.pack(expand=True)

        autor_frame.pack_propagate(False)
        autor_frame.pack(expand=True)

        title_label.pack(expand=True, fill="y")
        start_button.pack(side="left", expand=True)
        restart_button.pack(side="left", expand=True)
        stop_button.pack(side="left", expand=True)
        state_label.pack(expand=True)

        self.window.mainloop()

    def set_state_app(self, text) -> None:
        self.text_var.set(text)

    def stop_window(self) -> None:
        self.thread.stop()
