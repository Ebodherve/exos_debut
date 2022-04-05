
# Petit exercice utilisant la bibliothèque graphique tkinter
from tkinter import *
from random import randrange




x1,x2,y1,y2 = 0,120,0,120

fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1,bg='white',height=600,width=600)
can1.pack(side=LEFT)

for i in range(5) :
    can1.create_oval(x1+120*i,y1,x2+i*120,y2,width = 3, fill = "red")


bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)


fen1.mainloop() # démarrage du réceptionnaire d’événements

fen1.destroy() # destruction (fermeture) de la fenêtre




