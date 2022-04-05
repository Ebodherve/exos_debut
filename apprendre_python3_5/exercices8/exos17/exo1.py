
from tkinter import *



def deplace():
    global x,y,distance,r
    if x >= width_c :
        x,y = 0,400
    x += distance
    can1.coords(boule,x-r,y-r,x+r,y+r)
    


#création de l'objet fenetre
root = Tk()

#création du canvas
width_c = 800
height_c = 700
can1 = Canvas(root,width = width_c,height = height_c)

#création de la boule et des éléments nécessaires pour ca manipulation 
global x,y,r,distance
x,y,r,distance = 0,400,10,80


boule = can1.create_oval(x-r,y-r,x+r,y+r,fill = "red")


#boutton de deplacement 
bt1 = Button(root,text = "avancer",bg = "blue",command = deplace)


#placer le canvas et les bouttons
can1.grid()
bt1.grid()


#démarrage de la fenetre
root.mainloop()