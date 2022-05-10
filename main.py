from tkinter import *
from tkinter import filedialog as fd
import os

root = Tk()

class MenuOptions():
    def __init__(self):
        self.win2 = Tk()
        self.win2.mainloop()
        
    def AppConfig(self):
        self.win2.title("Preferências")
        self.win2.iconbitmap("image/duteblock_icon.ico")
        self.win2.geometry("")

class MenuArquivo():
    def ConfirmarAbrir(self):
        def Cancel():
            pop.destroy()
        def SalvarNovo():
            Cancel()
            self.SalvarComo()
            self.Open()
        def DontSave():
            Cancel()
            self.Open()
            
        
        pop = Tk()
        pop.title("Abrir Arquivo")
        pop.config(background= "#202020")
        pop.geometry("300x150")
        pop.iconbitmap("image/duteblock_icon.ico")
        pop.resizable(False, False)
        
        frame1 = Frame(pop, background= "#202020")
        frame1.place(relx= 0, rely= 0, relwidth= 1, relheight= 0.65)
        frame2 = Frame(pop, background= "#404040")
        frame2.place(relx= 0, rely= 0.7, relwidth= 1, relheight= 0.35)
        
        lbText = Label(frame1, text="Abrir novo documento sem salvar o atual?", background= "#202020", foreground="White", font=("Segoe UI", 10))
        lbText.place(relx=0, rely=0.35, relwidth= 0.94, relheight=0.7)
        lbName = Label(frame1, text="Dute Block", background= "#202020", foreground="White", font=("Segoe UI", 15, "bold"))
        lbName.place(relx= 0, rely=0.30, relwidth= 0.45, relheight= 0.2)
        
        btnSalv = Button(frame2, text="Salvar", background="#f43838", bd= 0, fg="white", command= SalvarNovo)
        btnSalv.place(relx= 0.05, rely=0.2, relwidth= 0.25, relheight= 0.4)
        btnDontSlv = Button(frame2, text="Não Salvar", background= "#202020", fg= "white", bd= 0, command= DontSave)
        btnDontSlv.place(relx= 0.375, rely=0.2, relwidth= 0.25, relheight= 0.4)
        BtnCancel = Button(frame2, text="Cancelar", background="#202020", bd= 0, fg= "white", command= Cancel)
        BtnCancel.place(relx= 0.7, rely=0.2, relwidth= 0.25, relheight= 0.4)
        
        pop.mainloop()
    
    def ConfirmarNovo(self):
        
        def Cancel():
            pop.destroy()
        def SalvarNovo():
            Cancel()
            self.SalvarComo()
        def DontSave():
            self.txt.delete(1.0, END)
            self.file = None
            self.win1.title("Novo Documento" + " - Dute Block")
            Cancel()
            
        
        pop = Tk()
        pop.title("Novo Arquivo")
        pop.config(background= "#202020")
        pop.geometry("300x150")
        pop.iconbitmap("image/duteblock_icon.ico")
        pop.resizable(False, False)
        
        frame1 = Frame(pop, background= "#202020")
        frame1.place(relx= 0, rely= 0, relwidth= 1, relheight= 0.65)
        frame2 = Frame(pop, background= "#404040")
        frame2.place(relx= 0, rely= 0.7, relwidth= 1, relheight= 0.35)
        
        lbText = Label(frame1, text="Criar novo documento sem salvar o atual?", background= "#202020", foreground="White", font=("Segoe UI", 10))
        lbText.place(relx=0, rely=0.35, relwidth= 0.94, relheight=0.7)
        lbName = Label(frame1, text="Dute Block", background= "#202020", foreground="White", font=("Segoe UI", 15, "bold"))
        lbName.place(relx= 0, rely=0.30, relwidth= 0.45, relheight= 0.2)
        
        btnSalv = Button(frame2, text="Salvar", background="#f43838", bd= 0, fg="white", command= SalvarNovo)
        btnSalv.place(relx= 0.05, rely=0.2, relwidth= 0.25, relheight= 0.4)
        btnDontSlv = Button(frame2, text="Não Salvar", background= "#202020", fg= "white", bd= 0, command= DontSave)
        btnDontSlv.place(relx= 0.375, rely=0.2, relwidth= 0.25, relheight= 0.4)
        BtnCancel = Button(frame2, text="Cancelar", background="#202020", bd= 0, fg= "white", command= Cancel)
        BtnCancel.place(relx= 0.7, rely=0.2, relwidth= 0.25, relheight= 0.4)
        
        pop.mainloop()
    
    def File(self):
        self.file = None
    def Open(self):
        filetyp = (("Arquivos de Texto", "*.txt"), ("Todos Arquivos", "*.*"))
        self.file = fd.askopenfilename(title= "Selecionar Nota", initialdir="/", filetypes=filetyp)
        basename = os.path.basename(self.file)
        filename = os.path.splitext(basename)[0]
        
        if filename != "":
            with open(self.file, "r", encoding="utf-8") as f:
                self.txt.delete(1.0, END)
                self.win1.title(filename + " - Dute Block")
                self.txt.insert(1.0, f.read())
        else:
            self.file = None
        
    def AbrirArquivo(self):
        identi = self.txt.get(1.0, END).strip()
        
        if(identi == ""):
            self.Open()
        else:
            self.ConfirmarAbrir()
            
            
            
    def Salvar(self):
        id = self.txt.get(1.0, END).strip()
        if(id != ""):
            filetypS = (("Documento de Texto (.txt)", "*.txt"), ("PDF (.pdf)", "*.pdf"))
            
            if(self.file != None):
                newText = self.txt.get(1.0, END)
                basename = os.path.basename(self.file)
                filename = os.path.splitext(basename)[0]
                with open(self.file, "w", encoding="utf-8") as f:
                    f.write(newText)
                    self.win1.title(filename + " - Dute Block")
            else:
                newText = self.txt.get(1.0, END)
                self.file = fd.asksaveasfilename(title="Salvar", initialdir="/", initialfile="Novo Documento.txt", filetypes= filetypS)
                basename = os.path.basename(self.file)
                filename = os.path.splitext(basename)[0]
                if filename != "":
                    with open(self.file + ".txt", "w", encoding="utf-8") as w:
                        w.write(newText)
                        self.win1.title(filename + " - Dute Block")
                else:
                    self.file = None
                
    def SalvarComo(self):
        filetypS = (("Documento de Texto (.txt)", "*.txt"), ("PDF (.pdf)", "*.pdf"))
        
        newText = self.txt.get(1.0, END)
        self.file = fd.asksaveasfilename(title="Salvar Como", initialdir="/", initialfile="Novo Documento.txt", filetypes= filetypS)
        basename = os.path.basename(self.file)
        filename = os.path.splitext(basename)[0]
        if(filename != ""):
            with open(self.file + ".txt", "w", encoding="utf-8") as w:
                w.write(newText)
                self.win1.title(filename + " - Dute Block")
        else:
            self.file = None
            
    def Novo(self):
        
        atual = self.txt.get(1.0, END).strip()
        if atual == "":
            self.txt.delete(1.0, END)
            self.file = None
            self.win1.title("Novo Documento" + " - Dute Block")
        else:
            self.ConfirmarNovo()

class Application(MenuArquivo):
    def __init__(self):
        self.win1 = root
        self.Config()
        self.Frames1()
        self.Widgets1()
        self.Menu1()
        self.File()
        root.mainloop()
        
    def Config(self):
        self.win1.title("Novo Documento - Dute Block")
        self.win1.configure(background= "#202020")
        self.win1.iconbitmap("image/duteblock_icon.ico")
        self.win1.geometry("500x400")
        self.win1.resizable(True, True)
        
    def Frames1(self):
        self.fr = Frame(self.win1, background= "#202020")
        self.fr.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        
    def Widgets1(self):
        self.txt = Text(self.fr, background= "#202020", fg= "white", font= ("Lucida Console", 12), border=0, wrap= WORD)
        self.txt.place(relx= 0.01, rely= 0.02, relwidth= 0.98, relheight= 0.96)
        
    def Menu1(self):
        self.menu = Menu(self.win1)
        
        self.fileMenu = Menu(self.menu, tearoff= 0)
        self.fileMenu.add_command(label= "Novo                            Ctrl-N", command= MenuOptions)
        self.fileMenu.add_command(label= "Abir                              Ctrl-O", command= self.AbrirArquivo)
        self.fileMenu.add_command(label= "Salvar                            Ctrl-S", command= self.Salvar)
        self.fileMenu.add_command(label= "Salvar Como         Ctrl-Alt-S", command= self.SalvarComo)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label= "Sair")
        self.menu.add_cascade(label= "Arquivo", menu= self.fileMenu)
        
        self.win1.config(menu= self.menu)
        #self.win1.bind("<Control-o>", lambda evento: self.AbrirArquivo(None))
        #self.win1.bind("<Control-n>", lambda evento: self.Novo(None))
        #self.win1.bind("<Control-s>", lambda evento: self.Salvar(None))
        #self.win1.bind("<Control-Alt-s>", lambda evento: self.SalvarComo(None))
        
        
Application()