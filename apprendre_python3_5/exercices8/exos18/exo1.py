

from tkinter import *
import math

#fonctions nécessaires pour la trajectoire circulaire
def coord_angle(x,y,r,a):
    return x+r*math.cos(a),y+r*math.sin(a)

#fonction de déplacement de la boule
def deplace_unit():
    global x_ctra,y_ctra,angle,r,rayon_traject
    
    x,y = coord_angle(x_ctra,y_ctra,rayon_traject,angle)
    can1.coords(boule,x-r,y-r,x+r,y+r)
    angle += 0.2

def deplace():
    for i in range(5):
        deplace_unit()


#création de l'objet fenetre
root = Tk()

#création du canvas
width_c = 800
height_c = 700
can1 = Canvas(root,width = width_c,height = height_c)

#création de la boule et des éléments nécessaires pour ca manipulation 
global x_traject,y_traject,r,angle,rayon_traject
x_ctra,y_ctra,r,angle,rayon_traject = 400,400,10,0.2,100
x,y = coord_angle(x_ctra,y_ctra,rayon_traject,0)

boule = can1.create_oval(x-r,y-r,x+r,y+r,fill = "red")


#boutton de deplacement 
bt1 = Button(root,text = "avancer",bg = "blue",command = deplace)


#placer le canvas et les bouttons
can1.grid()
bt1.grid()


#démarrage de la fenetre
root.mainloop()



