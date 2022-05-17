from tkinter import Tk


from tkinter import *

class Opcoes:
    def __init__(self):  
        self.win3 = Tk()
        self.OpConfig()
        self.Frame03()
        self.Widgets03()
        self.win3.mainloop()
        
    def OpConfig(self):
        self.win3.title("Preferências")
        self.win3.config(background= "#202020")
        self.win3.iconbitmap("image/duteblock_icon.ico")
        self.win3.geometry("300x125")
        
    def Frame03(self):
        self.frame03 = Frame(self.win3, background= "#202020", bd= 0)
        self.frame03.place(relx=0, rely=0, relheight=1, relwidth=1)
        
    def Widgets03(self):
        self.lb03 = Label(self.frame03, text= "Font Family", background= "#202020", fg= "#434343", font= ("Montsserat", 15))
        self.lb03.place(relx= 0.05, rely= 0.15, relheight= 0.2, relwidth= 0.35)
        self.lb04 = Label(self.frame03, text= "Font Size", background= "#202020", fg= "#434343", font= ("Montsserat", 15))
        self.lb04.place(relx= 0.044, rely= 0.4, relheight= 0.2, relwidth= 0.3)
        self.lb05 = Label(self.frame03, text= "Theme", background= "#202020", fg= "#434343", font= ("Montsserat", 15))
        self.lb05.place(relx= 0.06, rely= 0.65, relheight= 0.2, relwidth= 0.2)
        
Opcoes()