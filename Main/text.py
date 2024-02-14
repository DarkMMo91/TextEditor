import random
from tkinter import *
from tkinter import filedialog

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
root.iconbitmap("Main/Teditor_Icon.ico")

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


    
#Funzioni della SottoBar

#Label
InputField= Text(root, width=232, border=5, background=color)

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


MainBar.add_cascade(label="File", menu=filemenu)
MainBar.add_cascade(label="Altro" , menu=ReferenceMenu)
MainBar.add_cascade(label="Funzioni", menu=FuncMenu)


#Posizioni
InputField.grid(row=1, column=0, ipady=256)

#MainLoop ed altro

root.config(menu=MainBar)
root.mainloop()
