
from tkinter import *
import math  



#calcule la distance entre les duex astres
def distance():
    return math.sqrt((x1-x2)**2+(y1-y2)**2) 

#deplacement d'un astre
def deplace_ast(event):
    global choix_ast,x1,y1,x2,y2,r1,r2
    if  choix_ast :
        x1 = event.x
        y1 = event.y
        can.coords(ast1,x1-r1,y1-r1,x1+r1,y1+r1)
        labf.configure(text = "distance entre les astres : "+str(distance()))
        labd.configure(text = "force d'attraction  : "+str(force_atract()))
    else :
        x2 = event.x
        y2 = event.y
        can.coords(ast2,x2-r2,y2-r2,x2+r2,y2+r2)
        labf.configure(text = "distance entre les astres : "+str(distance()))
        labd.configure(text = "force d'attraction  : "+str(force_atract()))
    

#calcul de la force d'attraction entre les deux astres 
def force_atract():
    global G,m1,m2
    return G*m1*m2/(distance())



def change_choice() :
    global choix_ast
    choix_ast = (choix_ast & False)|(not choix_ast & True)



#coordonnées des deux astres
global x1,y1,x2,y2
x1,y1,x2,y2 = 50,100,400,100 

#rayon des deux astres et masses
global r1,r2,m1,m2,G
r1,r2,m1,m2 = 10,20,80,90
G = 6.67*(10**(-11))

#choix d'un astre
global choix_ast
choix_ast = True

#fenetre
root = Tk()

#canvas
can = Canvas(root,bg = "grey", width = 600, height = 600)

#gestion du deplacment des astres au clic de la souris
can.bind("<Button-1>",deplace_ast)

#astre 1
ast1 = can.create_oval(x1-r1,y1-r1,x1+r1,y1+r1,fill = "orange")
ast2 = can.create_oval(x2-r2,y2-r2,x2+r2,y2+r2,fill = "blue")

#labels d'affichage des masses des deux boules  
lab1 = Label(root,text = "astre orange, masse : "+str(m1),width = 75, bg = "orange")

lab2 = Label(root,text = "astre bleu, masse : "+str(m2),width = 75, bg = "blue")

#labels d'affichage des distances et forces d'attraction entre les deux boulles  
labd = Label(root,text = "distance entre les astres : "+str(distance()), width = 75, bg = "yellow")

labf = Label(root,text = "force d'attraction  : "+str(force_atract()), width = 75, bg = "red")



#deplace un astre à droite
bc = Button(root,text = "changer d'astre",command = change_choice)  

#boutton permettant de quitter la fenetre
bq = Button(root,text = "quitter", command = root.quit)

lab1.grid(row = 1)
lab2.grid(row = 2)

can.grid(row = 3,rowspan = 50)

labf.grid(row = 53,sticky = S)
labd.grid(row = 54,sticky = S)

bc.grid(row = 5,column = 2,sticky = N)
bq.grid(row = 52,column = 2,sticky = N)

#démarrage de l'interface gaphique
root.mainloop()


