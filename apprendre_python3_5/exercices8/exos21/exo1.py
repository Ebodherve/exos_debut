
from tkinter import *


#créations de rectangles jaunes pour piéton
def rect_jaune(ht,larg):
    h = ht//2
    l = larg//2
    x1,y1 = 100+l,250    
    for i in range(x1,400-l,larg+20):
        can1.create_rectangle(i-l,y1-h,i+l,y1+h,fill = "yellow")


#changement de couleurs des boules
def changer():
    global etat_feu
    if etat_feu :
        cg1 = can1.create_oval(x1g+r1,y1g+r1,x1g-r1,y1g-r1,fill = "red")
        cg2 = can1.create_oval(x2g+r2,y2g+r2,x2g-r2,y2g-r2,fill = "light green")
        cd1 = can1.create_oval(x1d+r1,y1d+r1,x1d-r1,y1d-r1,fill = "red")
        cd2 = can1.create_oval(x2d+r2,y2d+r2,x2d-r2,y2d-r2,fill = "light green")
        etat_feu = False
    else :
        cg1 = can1.create_oval(x1g+r1,y1g+r1,x1g-r1,y1g-r1,fill = "light green")
        cg2 = can1.create_oval(x2g+r2,y2g+r2,x2g-r2,y2g-r2,fill = "red")
        cd1 = can1.create_oval(x1d+r1,y1d+r1,x1d-r1,y1d-r1,fill = "light green")
        cd2 = can1.create_oval(x2d+r2,y2d+r2,x2d-r2,y2d-r2,fill = "red")
        etat_feu = True
        
    


#fenetre principale
root =  Tk()

#canevas pour les objets
can1 = Canvas(root,width = 500,height = 500,bg = "light gray")

#variable symbolisant l'état des feux
global etat_feu
etat_feu = True

#création du rectangle
rect = can1.create_rectangle(100,500,400,0,fill = "gray")

#crétion des cercles gauches et droits
x1g,y1g,x2g,y2g = 75,150,75,350
x1d,y1d,x2d,y2d = 425,350,425,150
r1 = 20
r2 = 15
#gauche
cg1 = can1.create_oval(x1g+r1,y1g+r1,x1g-r1,y1g-r1,fill = "light green")
cg2 = can1.create_oval(x2g+r2,y2g+r2,x2g-r2,y2g-r2,fill = "red")
cd1 = can1.create_oval(x1d+r1,y1d+r1,x1d-r1,y1d-r1,fill = "light green")
cd2 = can1.create_oval(x2d+r2,y2d+r2,x2d-r2,y2d-r2,fill = "red")

#rectangle jaune pour pietons
rect_jaune(150,25) 

#boutton de changement des feux de circulation 
btc = Button(root,text = "changer",command = changer)

#disposition des objets
can1.grid()
btc.grid(sticky = E)

#demarrage de l'interface graphique
root.mainloop() 
