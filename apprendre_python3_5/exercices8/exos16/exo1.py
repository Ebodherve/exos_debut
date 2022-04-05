#TF =TC ×1,80+32

from tkinter import *


def convert_fc(event):
   affiche1.configure(text ="temperature en degré celsius : "+ str(((eval(entrec.get()))-32)/1.8))

def convert_cf(event):
    affiche2.configure(text ="temperature en degré Fahrenheit : "+str(((eval(entrec.get()))*1.8)+32))


root = Tk()

#objets d'entrées des valeurs
entrec = Entry(root)
entrec.bind("<Return>",convert_cf)
entref = Entry(root)
entref.bind("<Return>",convert_fc)

#objets d'affichage du message de demande pour les entrée
affiche1 = Label(root,text = "temperature en degré celsius : ")
affiche2 = Label(root,text = "temperature en degré Fahrenheit : ")

#disposition des objets
affiche1.grid(row = 1,column = 1)
affiche2.grid(row = 2,column = 1)

entrec.grid(row = 1, column = 2)
entref.grid(row = 2, column = 2)

#demarrage de l'interface
root.mainloop()

