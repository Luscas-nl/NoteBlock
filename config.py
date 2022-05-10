import main as m
from tkinter import *

root = Tk()

class Configuration():
    def __init__(self):
        self.win = root
        self.Config()
        root.mainloop()
        
    def Config(self):
        self.win.title = "Configurações"