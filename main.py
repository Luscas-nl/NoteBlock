from tkinter import *
from tkinter import filedialog as fd
from tkinter import font
import os

class MenuEditar():
    
    def Theme(self):
        temaAtual = self.strTH.get().upper()
        
        if temaAtual == "LIGHT":
            self.txt.configure(fg= "black", background= "white")
            self.fr.configure(background= "white")

        else:
            self.txt.configure(fg= "white", background= "#202020")
            self.fr.configure(background= "#202020")
    
    def FontStile(self):
        fontS = font.Font(self.txt, self.txt.cget("font"))
        fontS.configure(size= int(self.strFS.get()), family= self.strFF.get())
        self.txt.tag_configure("FontStile", font= fontS)
        self.txt.tag_add("FontStile", 1.0, END)
        
    def Selecao(self):
        self.selecionado = False
    def Recortar(self):
        if self.txt.selection_get():
            self.selecionado = self.txt.selection_get()
            self.win1.clipboard_clear()
            self.win1.clipboard_append(self.selecionado)
            self.txt.delete("sel.first", "sel.last")
    def Colar(self):
        self.selecionado = self.win1.clipboard_get()
        if self.selecionado != "":
            posicao = self.txt.index(INSERT)
            self.txt.insert(posicao, self.selecionado)  
    def Copiar(self):
        if self.txt.selection_get():
            self.selecionado = self.txt.selection_get()
            self.win1.clipboard_clear()
            self.win1.clipboard_append(self.selecionado) 
    def Bold(self):
        if self.txt.selection_get():
            boldFont = font.Font(self.txt, self.txt.cget("font"))
            boldFont.configure(weight= "bold")
            
            self.txt.tag_configure("bold", font= boldFont)
            tag = self.txt.tag_names("sel.first")
            
            if "bold" in tag:
                self.txt.tag_remove("bold", "sel.first", "sel.last")
            else:
                if "italic" in tag:
                    self.txt.tag_remove("italic", "sel.first", "sel.last")
                self.txt.tag_add("bold", "sel.first", "sel.last")
    def Italic(self):
        if self.txt.selection_get():
            italicFont = font.Font(self.txt, self.txt.cget("font"))
            italicFont.configure(slant= "italic")
            
            self.txt.tag_configure("italic", font= italicFont)
            tag = self.txt.tag_names("sel.first")
            
            if "italic" in tag:
                self.txt.tag_remove("italic", "sel.first", "sel.last")
            else:
                if "bold" in tag:
                    self.txt.tag_remove("bold", "sel.first", "sel.last")
                self.txt.tag_add("italic", "sel.first", "sel.last")
    
    def Opcoes(self): 
        self.win3 = Tk()
        self.win3.title("Preferências")
        self.win3.config(background= "#202020")
        self.win3.iconbitmap("image/duteblock_icon.ico")
        
        x = (self.screenW / 2) - (300 / 2)
        y = (self.screenH / 2) - (125 / 2)
        self.win3.geometry(f"300x125+{int(x)}+{int(y)}")
        
        self.frame03 = Frame(self.win3, background= "#202020", bd= 0)
        self.frame03.place(relx=0, rely=0, relheight=1, relwidth=1)
        
        self.lb03 = Label(self.frame03, text= "Font Family", background= "#202020", fg= "#434343", font= ("Montsserat", 15))
        self.lb03.place(relx= 0.05, rely= 0.15, relheight= 0.2, relwidth= 0.35)
        self.lb04 = Label(self.frame03, text= "Font Size", background= "#202020", fg= "#434343", font= ("Montsserat", 15))
        self.lb04.place(relx= 0.044, rely= 0.4, relheight= 0.2, relwidth= 0.3)
        self.lb05 = Label(self.frame03, text= "Theme", background= "#202020", fg= "#434343", font= ("Montsserat", 15))
        self.lb05.place(relx= 0.06, rely= 0.65, relheight= 0.2, relwidth= 0.2)
        
        self.strFS = StringVar(self.frame03)
        self.strFS.set("12")
        self.tipFS = ("8", "9", "10", "11", "12", "14", "16", "18", "20", "22", "24", "26", "28", "36", "48", "72")
        self.optFS = OptionMenu(self.frame03, self.strFS, *self.tipFS, command= lambda x: self.FontStile())
        self.optFS.config(bg="#111111", font= ("Montsserat", 8), fg= "white", bd= 0, highlightthickness= 0.5, highlightbackground= "#434343", )
        self.optFS.place(relx= 0.35, rely= 0.4, relwidth= 0.59, relheight= 0.2)
        
        self.strFF = StringVar(self.frame03)
        self.strFF.set("Lucida Console")
        self.tipFF = ("Arial", "Lucida Console", "Montsserat", "Times New Roman")
        self.optFF = OptionMenu(self.frame03, self.strFF, *self.tipFF, command= lambda x: self.FontStile())
        self.optFF.config(bg="#111111", font= ("Montsserat", 8), fg= "white", bd= 0, highlightthickness= 0.5, highlightbackground= "#434343", )
        self.optFF.place(relx= 0.42, rely= 0.15, relwidth= 0.52, relheight= 0.2)
        
        self.strTH = StringVar(self.frame03)
        self.strTH.set("Dark")
        self.tipTH = ("Dark", "Light")
        self.optTH = OptionMenu(self.frame03, self.strTH, *self.tipTH, command= lambda x: self.Theme())
        self.optTH.config(bg="#111111", font= ("Montsserat", 8), fg= "white", bd= 0, highlightthickness= 0.5, highlightbackground= "#434343", )
        self.optTH.place(relx= 0.28, rely= 0.65, relwidth= 0.66, relheight= 0.2)
        self.win3.mainloop()

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
        x = (self.screenW / 2) - (300 / 2)
        y = (self.screenH / 2) - (100 / 2)
        pop.geometry(f"300x100+{int(x)}+{int(y)}")
        pop.iconbitmap("image/duteblock_icon.ico")
        pop.resizable(False, False)

        frame1 = Frame(pop, background= "#202020")
        frame1.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)

        lbText = Label(frame1, text="Criar novo documento sem salvar o atual? ", background= "#202020", foreground="#434343", font=("Montsserrat", 10))
        lbText.place(relx=0, rely=0.1, relwidth= 1, relheight=0.7)
        lbName = Label(frame1, text="Dute Block", background= "#202020", foreground="#434343", font=("Montsserrat", 15, "bold"))
        lbName.place(relx= 0.032, rely=0.15, relwidth= 0.45, relheight= 0.2)

        btnSalv = Button(frame1, text="Salvar", background="#111111", bd= 0, fg="white", font=("Montsserrat", 8), command= SalvarNovo)
        btnSalv.place(relx= 0.09, rely=0.6, relwidth= 0.25, relheight= 0.2)
        btnDontSlv = Button(frame1, text="Não Salvar", background= "#111111", bd= 0, fg= "white", font=("Montsserrat", 8), command= DontSave)
        btnDontSlv.place(relx= 0.374, rely=0.6, relwidth= 0.25, relheight= 0.2)
        BtnCancel = Button(frame1, text="Cancelar", background="#111111", bd= 0, fg= "white", font=("Montsserrat", 8), command= Cancel)
        BtnCancel.place(relx= 0.66, rely=0.6, relwidth= 0.25, relheight= 0.2)

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
        x = (self.screenW / 2) - (300 / 2)
        y = (self.screenH / 2) - (100 / 2)
        pop.geometry(f"300x100+{int(x)}+{int(y)}")
        pop.iconbitmap("image/duteblock_icon.ico")
        pop.resizable(False, False)

        frame1 = Frame(pop, background= "#202020")
        frame1.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)

        lbText = Label(frame1, text="Abrir novo documento sem salvar o atual? ", background= "#202020", foreground="#434343", font=("Montsserrat", 10))
        lbText.place(relx=0, rely=0.1, relwidth= 1, relheight=0.7)
        lbName = Label(frame1, text="Dute Block", background= "#202020", foreground="#434343", font=("Montsserrat", 15, "bold"))
        lbName.place(relx= 0.032, rely=0.15, relwidth= 0.45, relheight= 0.2)

        btnSalv = Button(frame1, text="Salvar", background="#111111", bd= 0, fg="white", font=("Montsserrat", 8), command= SalvarNovo)
        btnSalv.place(relx= 0.09, rely=0.6, relwidth= 0.25, relheight= 0.2)
        btnDontSlv = Button(frame1, text="Não Salvar", background= "#111111", bd= 0, fg= "white", font=("Montsserrat", 8), command= DontSave)
        btnDontSlv.place(relx= 0.374, rely=0.6, relwidth= 0.25, relheight= 0.2)
        BtnCancel = Button(frame1, text="Cancelar", background="#111111", bd= 0, fg= "white", font=("Montsserrat", 8), command= Cancel)
        BtnCancel.place(relx= 0.66, rely=0.6, relwidth= 0.25, relheight= 0.2)

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


class Application(MenuArquivo, MenuEditar):
    def __init__(self):
        self.win1 = Tk()
        self.dark = True
        self.Config()
        self.Frames1()
        self.Widgets1()
        self.Menu1()
        self.File()
        self.win1.mainloop()
        
    def Config(self):
        self.screenW = self.win1.winfo_screenwidth()
        self.screenH = self.win1.winfo_screenheight()
        x = (self.screenW / 2) - (500 / 2)
        y = (self.screenH / 2) - (400 / 2)
        
        self.win1.title("Novo Documento - Dute Block")
        self.win1.configure(background= "#202020")
        self.win1.iconbitmap("image/duteblock_icon.ico")
        self.win1.geometry(f"500x400+{int(x)}+{int(y)}")
        self.win1.resizable(True, True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        
    def Frames1(self):
        self.fr = Frame(self.win1, background= "#202020")
        self.fr.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        
    def Widgets1(self):
        self.txt = Text(self.fr, background= "#202020", undo= True, fg= "white", font= ("Lucida Console", 12), border=0, wrap= WORD)
        self.txt.place(relx= 0.01, rely= 0.02, relwidth= 0.98, relheight= 0.96)
        
    def Menu1(self):
        self.menu = Menu(self.win1)
        
        self.fileMenu = Menu(self.menu, tearoff= False)
        self.fileMenu.add_command(label= "Novo                            Ctrl-N", command= self.Novo)
        self.fileMenu.add_command(label= "Abir                              Ctrl-O", command= self.AbrirArquivo)
        self.fileMenu.add_command(label= "Salvar                            Ctrl-S", command= self.Salvar)
        self.fileMenu.add_command(label= "Salvar Como         Ctrl-Alt-S", command= self.SalvarComo)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label= "Sair")
        self.menu.add_cascade(label= "Arquivo", menu= self.fileMenu)
        
        self.editMenu = Menu(self.menu, tearoff= False)
        self.editMenu.add_command(label= "Desfazer                  Ctrl-Z", command= self.txt.edit_undo)
        self.editMenu.add_command(label= "Refazer                    Ctrl-Y", command= self.txt.edit_redo)
        self.editMenu.add_separator()
        self.editMenu.add_command(label= "Recortar                  Ctrl-X", command= self.Recortar)
        self.editMenu.add_command(label= "Copiar                     Ctrl-C", command= self.Copiar)
        self.editMenu.add_command(label= "Colar                       Ctrl-V", command= self.Colar)
        self.editMenu.add_separator()
        self.editMenu.add_command(label= "Preferências           Ctrl-P", command= self.Opcoes)
        self.menu.add_cascade(label= "Editar", menu= self.editMenu)
        
        self.win1.config(menu= self.menu)
        self.win1.bind("<Control-Key-o>", lambda x: self.AbrirArquivo())
        self.win1.bind("<Control-Key-n>", lambda x: self.Novo())
        self.win1.bind("<Control-Key-s>", lambda x: self.Salvar())
        self.win1.bind("<Control-Alt-Key-s>", lambda x: self.SalvarComo())
        self.win1.bind("<Control-Key-b>", lambda x: self.Bold())
        self.win1.bind("<Control-Key-l>", lambda x: self.Italic())
        self.win1.bind("<Control-Key-p>", lambda x: self.Opcoes())
        
        
Application()