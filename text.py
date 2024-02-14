from tkinter import * 
from tkinter import ttk

#MainRoot
root = Tk()

#Constante

WHITE = "FFFFF"
#Variabili

root.geometry("820x820")
root.title("Teditor")
root.iconbitmap("C:/Users/39339/Desktop/Python/TextEditor/Teditor_Icon.ico")

#Funzioni

def FunzioneTest():
    print(InputField.get())
    return 0

#Label

SaveButton = Button(root, text="Salva", command=FunzioneTest, width=6)
FuncButton = Button(root, text="Funzioni", width=12)
RevisionButton = Button(root, text="Revisione")
HelpButton = Button(root, text="Help")
InputField= Entry(root, width=520, border=5)

#Posizioni
InputField.grid(row=1, column=5)

SaveButton.grid(row=0, column=0)
FuncButton.grid(row=0, column=1)
RevisionButton.grid(row=0, column=2)
HelpButton.grid(row=0, column=3)

#MainLoop
root.mainloop()
