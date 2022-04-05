from tkinter import *
from random import randint

fen = Tk()

lmain = []
global pierre,papier,ciseaux

pierre,papier,ciseaux = 0,0,0


lmain.append(PhotoImage(file = "pierre.gif"))
lmain.append(PhotoImage(file = "papier.gif"))
lmain.append(PhotoImage(file = "ciseaux.gif"))



for i in range(6) :
    #global pierre,papier,ciseaux
    b = Button(fen)
    b.grid(row = 0, column = i)
    choix = randint(0,2)
    b.configure(image = lmain[choix])
    if choix == 0 :
        pierre += 1
    elif choix == 1 :
        papier +=1
    else :
        ciseaux +=1
        



for i in range(6) :
    #global pierre,papier,ciseaux
    b = Button(fen)
    b.grid(row = 1, column = i)
    choix = randint(0,2)
    b.configure(image = lmain[choix])
    if choix == 0 :
        pierre += 1
    elif choix == 1 :
        papier +=1
    else :
        ciseaux +=1
    
    
historique = Toplevel()
historique.title("HISTORIQUE")
B1 = Button(historique,text = "nombre de pierre = "+str(pierre))
B1.grid(row = 1,column =1)
B2 = Button(historique,text = "nombre de papier = "+str(papier))
B2.grid(row = 1,column =2)
B3 = Button(historique,text = "nombre de ciseaux = "+str(ciseaux))
B3.grid(row = 1,column =3)



fen.mainloop()


