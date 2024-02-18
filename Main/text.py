import random
from tkinter import *
from tkinter import filedialog
from tkinter import font

#MainRoot
root = Tk()

#Constante

White = "white"
Black = "black"

#Variabili

color = White
#Variabili per la finestra

root.geometry("1280x720")
root.title("Teditor")
root.iconbitmap("IcoFile/Teditor_Icon.ico")

#Funzioni della MainBar

def Salva_file():
    global InputField
    file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("File di testo", ".txt"),
                                                                        ("File HTML" , ".html"),
                                                                        ("File CSS", ".css"),
                                                                        ("Tutti i file", ".*")])
    t = str(InputField.get("1.0", END))        
    file.write(t)
    file.close            

def Apri_file():
    filepath = filedialog.askopenfilename(title="Vuoi aprire un file?",filetypes=[("File di Testo", ".txt"), ("Tutti i tipi di file", ".*")])

    file = open(filepath, "r")
    read = file.read()
    InputField.insert(END, read)
    file.close()

def Riferimento():
    pass

def Quit_app():
    root.quit()

#Funzioni della MainBar // Sotto Menù funzioni
def Distruzione():
    InputField.delete("1.0", END)

def Generazione_numeri():
    r = random.randint(1, 10000)

    InputField.insert("1.0", str(r))

def Generazione_nomi():

    k = random.randint(0, 12)

    name_List = ("Pedro", "Alessando", "Maria", "Carlo", "Anthony", "Carla", "Alfredo", "Francesco", "Francesca", "Simone", "Daniel", "Antonio", "Jake")

    InputField.insert("1.0", name_List[k])

def Generazione_citta():
    r = random.randint(0, 9)

    list = ["Roma", "Berlino", "Foggia", "Barcellona", "Bari", "Barletta", "Molfetta", "Udine", "Torino", "Firenze"]

    InputField.insert("1.0", list[r])
#Funzioni della SottoBar
    
def Bold_it():
    bold_font = font.Font(InputField, InputField.cget("font"))
    bold_font.configure(weight="bold")

    InputField.tag_configure("bold", font=bold_font)

    current_tags = InputField.tag_names("sel.first")

    if "bold" in current_tags:
        InputField.tag_remove("bold", "sel.first", "sel.last")
    else:
        InputField.tag_add("bold", "sel.first", "sel.last")

def italic():
    italic_font = font.Font(InputField, InputField.cget("font"))
    italic_font.configure(slant="italic")

    InputField.tag_configure("italic", font=italic_font)

    current_tags = InputField.tag_names("sel.first")

    if "italic" in current_tags:
        InputField.tag_remove("italic", "sel.first", "sel.last")
    else:
        InputField.tag_add("italic", "sel.first", "sel.last")

def underline():
    
    underline_font = font.Font(InputField, InputField.cget("font"))
    underline_font.configure(underline=TRUE)

    InputField.tag_configure("underline", font=underline_font)

    current_tags = InputField.tag_names("sel.first")

    if "underline" in current_tags:
        InputField.tag_remove("underline", "sel.first", "sel.last")
    else:
        InputField.tag_add("underline", "sel.first", "sel.last")

def overstrike():
    
    overstrike_font = font.Font(InputField, InputField.cget("font"))
    overstrike_font.configure(overstrike=TRUE)

    InputField.tag_configure("over", font=overstrike_font)

    current_tags = InputField.tag_names("sel.first")

    if "over" in current_tags:
        InputField.tag_remove("over", "sel.first", "sel.last")
    else:
        InputField.tag_add("over", "sel.first", "sel.last")

def add_highlighter():
   InputField.tag_add("start", "sel.first","sel.last")
   InputField.tag_config("start", background= "yellow", foreground= "Black")

#Frame

tool_frame = Frame(root)
tool_frame.pack(fill=X)

#Font style
BoldFont = font.Font(size = 8, weight = "bold")
ItalicFont = font.Font(size = 8, slant="italic")
UnderlineFont = font.Font(size = 8, underline=TRUE)
OverstrikeFont = font.Font(size = 8, overstrike=TRUE)


#Label
InputField= Text(root, width=232, border=5, background=color)

Bold_Botton = Button(tool_frame, text="B", command=Bold_it , font=BoldFont, width=2)
Italic_Botton = Button(tool_frame, text="I", command=italic, font=ItalicFont, width=2)
Underline_Botton = Button(tool_frame, text="U", command=underline, font=UnderlineFont, width=2)
Overstrike_Botton = Button(tool_frame, text="S", command=overstrike, font=OverstrikeFont, width=2)
Highlight_Botton = Button(tool_frame, text="Evidenzia", command=add_highlighter)

#MainBAr

MainBar = Menu(root)

filemenu = Menu(MainBar, tearoff=0)

filemenu.add_command(label="Open", command=Apri_file)
filemenu.add_command(label="Save", command=Salva_file)
filemenu.add_command(label="Exit", command=Quit_app)

ReferenceMenu = Menu(MainBar, tearoff=0)

ReferenceMenu.add_command(label="Riferimento", command=Riferimento)


FuncMenu = Menu(MainBar, tearoff=0)

FuncMenu.add_command(label="Annientamento", command=Distruzione)
FuncMenu.add_command(label="Generatore di Numeri", command=Generazione_numeri)
FuncMenu.add_command(label="Generatore di Nomi", command=Generazione_nomi)
FuncMenu.add_command(label="Generatore di Città", command=Generazione_citta)


MainBar.add_cascade(label="File", menu=filemenu)
MainBar.add_cascade(label="Altro" , menu=ReferenceMenu)
MainBar.add_cascade(label="Funzioni", menu=FuncMenu)


#Posizioni
InputField.pack(side=LEFT, ipady=250)

Bold_Botton.grid(row=0, column=0, sticky=W)
Italic_Botton.grid(row=0, column=1)
Underline_Botton.grid(row=0, column=2)
Overstrike_Botton.grid(row=0, column=3)
Highlight_Botton.grid(row=0, column=4)
#MainLoop e config

root.config(menu=MainBar)
root.mainloop()
