"""objectif du programme : Faire tomber une boulle de manière à faire en 
sorte qu'elle rebondisse jusqu'à ce qu'elle s'arrete"""

from tkinter import *
import math

#déplacer la boulle à x,y
def deplace(x,y):
    space.coords(boulle,x-rb,y-rb,x+rb,y+rb)

#fonction qui permet de faire tomber la boulle
def tombe():
    #tunit
    global xb,yb,rb
    yb += 10 
#    yb += tunit 
    deplace(xb,yb)  
    if yb < hs-rb:
        root.after(10,tombe)
    else :
        root.after(10,bond)

#fonction permettant de faire un bond 
def bond():
    global xb,yb,rb,xc,yc,rtc,angle
    angle += 0.1
    xb = xc + rtc*math.cos(angle)
    yb = yc + rtc*math.sin(angle)
    deplace(xb,yb)
    if angle < 5:
        root.after(10,bond)
    elif rtc > 0:
        angle = 0
        rtc -= 5
        xc += rtc*2
        root.after(10,bond)
    else :
        pass
    
#Tomber et rebondir
def tombe_rebon():
    global xb,yb,rb,xc,yc,rc,angle
    tombe()
    


#fennetre principale
root = Tk()

#espace dans lequelle la boulle tombe
ws,hs = 800,800 
space = Canvas(root,width = ws,height = ws)

#creation de notre boulle et initialisation des coordonnées et du rayon
global xb,yb,rb
xb,yb,rb = 20,20,10
boulle = space.create_oval(xb-rb,yb-rb,xb+rb,yb+rb,fill = "orange")

#création des coordonnées du point centrale de la trajectoire circulaire 
# du rayon de cette trajectoire,ainsi que de l'angle de déplacement
global xc,yc,rtc,angle
xc,yc,rtc,angle = 70,800-rb,50,0 


#boutton qui déclenche le mouvement
bmove = Button(root, text = "fait tomber la boulle",command = tombe_rebon)


#adaptation of canvas and buttons

space.grid()
bmove.grid()

#demarrage de l'interface graphique
root.mainloop()
