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

def Salva_File():
    global InputField
    file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("File di testo", ".txt"),
                                                                        ("File HTML" , ".html"),
                                                                        ("File CSS", ".css"),
                                                                        ("Tutti i file", ".*")])
    t = str(InputField.get("1.0", END))        
    file.write(t)
    file.close            

def Apri_File():
    filepath = filedialog.askopenfilename(title="Vuoi aprire un file?",filetypes=[("File di Testo", ".txt"), ("Tutti i tipi di file", ".*")])

    file = open(filepath, "r")
    read = file.read()
    InputField.insert(END, read)
    file.close()

def Riferimento():
    pass

def Distruzione():
    InputField.delete("1.0", END)

def Generazione_numeri():
    r = random.randint(1, 10000)

    InputField.insert("1.0", str(r))

def Generazione_Nomi():

    k = random.randint(0, 7)

    name_List = ("Pedro", "Alessando", "Maria", "Carlo", "Anthony", "Carla", "Alfredo", "Francesco")

    InputField.insert("1.0", name_List[k])

#Funzioni della SottoBar
    
def Bold_it():
    bold_font = font.Font(InputField, InputField.cget("font"))
    bold_font.configure(weight="bold", size=28)

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

#Tuple


#Frame

tool_frame = Frame(root)
tool_frame.pack(fill=X)

#Label
InputField= Text(root, width=232, border=5, background=color)

Bold_Botton = Button(tool_frame, text="Bold", command=Bold_it)
Italic_Botton = Button(tool_frame, text="Italic", command=italic)

#MainBAr

MainBar = Menu(root)

filemenu = Menu(MainBar, tearoff=0)

filemenu.add_command(label="Open", command=Apri_File)
filemenu.add_command(label="Save", command=Salva_File)

ReferenceMenu = Menu(MainBar, tearoff=0)

ReferenceMenu.add_command(label="Riferimento", command=Riferimento)


FuncMenu = Menu(MainBar, tearoff=0)

FuncMenu.add_command(label="Annientamento", command=Distruzione)
FuncMenu.add_command(label="Generazione di Numeri", command=Generazione_numeri)
FuncMenu.add_command(label="Generazione di Nomi", command=Generazione_Nomi)


MainBar.add_cascade(label="File", menu=filemenu)
MainBar.add_cascade(label="Altro" , menu=ReferenceMenu)
MainBar.add_cascade(label="Funzioni", menu=FuncMenu)


#Posizioni
InputField.pack(side=LEFT, ipady=250)

Bold_Botton.grid(row=0, column=0, sticky=W)
Italic_Botton.grid(row=0, column=1)

#MainLoop e config

root.config(menu=MainBar)
root.mainloop()
