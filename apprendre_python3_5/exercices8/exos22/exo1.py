
from tkinter import *
import math as m


#fonction de modification des resistance et tension
def modif_r(event):
    global ouvert,resistance, tension, intensite
    if not ouvert:
        resistance = float(eval(entre_r.get()))
        tension = resistance*intensite
    etiq_r.configure(text = "resistance = "+str(resistance))
    etiq_t.configure(text = "tension = "+str(tension))

def modif_t(event):
    global ouvert,resistance, tension, intensite
    if not ouvert:
        tension = float((eval(entre_t.get())))
        resistance = tension/intensite
    etiq_r.configure(text = "resistance = "+str(resistance))
    etiq_t.configure(text = "tension = "+str(tension))

def f_o_inter():
    global ouvert,resistance, tension, intensite
    if ouvert :
        can1.coords(filpi,200,380,220,380)
        resistance, tension, intensite = 10,20,2 
        etiq_i.configure(text = "intensite = "+str(intensite))
        etiq_r.configure(text = "resistance = "+str(resistance))
        etiq_t.configure(text = "tension = "+str(tension))
        
        b_interrupt.configure(text = "ouvrir l'interrupteur")
        ouvert = False
    else :
        can1.coords(filpi,200,380,200,390)
        resistance, tension, intensite = 0,0,0
        etiq_i.configure(text = "intensite = "+str(intensite))
        etiq_r.configure(text = "resistance = "+str(resistance))
        etiq_t.configure(text = "tension = "+str(tension))

        b_interrupt.configure(text = "fermer l'interrupteur")
        ouvert = True
    





#fenetre
root = Tk()

#le canvas et ses dimensions
w = 700
h = 700
can1 = Canvas(root,width = w,height = h)

#création des objets du canvas


#création du generateur hauteur = 300 largeur = 20
generateur = can1.create_rectangle(80,80,100,380,fill = "green")

#création du fil conducteur
filp1 = can1.create_line(100,380,200,380,fill = "black")
filp2 = can1.create_line(220,380,400,380,fill = "black")
filp3 = can1.create_line(400,380,400,280,fill = "black")

filp4 = can1.create_line(80,80,400,80,fill = "black")
filp5 = can1.create_line(400,80,400,180,fill = "black")

#interrupteur
global ouvert
ouvert = False

filpi = can1.create_line(200,380,220,380,fill = "gray")

#résistance et tension
global resistance, tension, intensite
resistance, tension, intensite = 10,20,2 

entre_r = Entry(root)
entre_r.bind("<Return>",modif_r)

entre_t = Entry(root)
entre_t.bind("<Return>",modif_t)

#etiquettes d'affiche de l'intensite,la tension et la résistance
etiq_i = Label(root,text = "intensite = "+str(intensite),bg="gray")
etiq_t = Label(root,text = "tension = "+str(tension),bg="gray",width = 15)
etiq_r = Label(root,text = "resistance = "+str(resistance),bg="gray",width = 15)

#boutton d'ouverture et de fermeture de l'interrupteur
b_interrupt = Button(root,text="ouvrir l'interrupteur",command = f_o_inter,width = 20)

#création du generateur hauteur = 300 largeur = 20
resistance = can1.create_rectangle(380,180,400,280,fill = "red")



#disposition des widgets
can1.grid(column = 1,rowspan = 50,columnspan = 50)

etiq_i.grid(row = 1,column = 51)
etiq_t.grid(row = 51,column = 1)
entre_t.grid(row = 51,column = 2)

etiq_r.grid(row = 52,column = 1)
entre_r.grid(row = 52,column = 2)

b_interrupt.grid(row = 51,column=51)
Button(root,text = "Quitter",bg = "gray",command = root.quit).grid(row = 52,column=51)

#démarrage de l'interface graphique
root.mainloop()



