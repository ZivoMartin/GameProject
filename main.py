import tkinter as tk
from view import View
from model import Model
from controller import Controller

class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        model = Model(self, 7)
        view = View(self, 7)
        controller = Controller(model, view)

app = Application()
app.mainloop()