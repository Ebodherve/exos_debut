from tkinter import *
from random import randint


def rect(x,y,c,coul):
    can1.create_rectangle(x-c/2,y-c/2,x+c/2,y+c/2,fill = coul)
    
def cercle(x,y,c,coul):
    can1.create_oval(x-c/2,y-c/2,x+c/2,y+c/2,fill = coul)

def dam():
    global ind_noire
    ind_noire = 0
    x=25
    y=25
    for i in range(10):
        x = 25
        for j in range(10) :
            indcoul = (j+i)%len(lcoul)
            if lcoul[indcoul] == "white":
                l_coord_noire.append([x,y,50])
            rect(x,y,50,lcoul[indcoul])
            x += 50
        y += 50
                
def pion_rouge():
    ind = randint(0,len(l_coord_noire)-1)
    cercle(l_coord_noire[ind][0],l_coord_noire[ind][1],l_coord_noire[ind][2]-5,"red")
    

lcoul = ["blue","white"]
root = Tk()
global ind_noire
ind_noire = 0
l_coord_noire = []

can1 = Canvas(root,bg="gray", width = 500, height = 500)
can1.pack()

b1 = Button(root,text = "damier", command = dam)
b1.pack(side = LEFT)

b2 = Button(root, text = "pions", command = pion_rouge)
b2.pack(side = RIGHT)

dam()

root.mainloop()


