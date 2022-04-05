from tkinter import *


def rect(x,y,c,coul):
    can1.create_rectangle(x-c/2,y-c/2,x+c/2,y+c/2,fill = coul)
    

def dam(c):
    x=25
    y=25
    for i in range(10):
        x = 25
        for j in range(10) :
            indcoul = (j+i)%len(lcoul)
            if lcoul[indcoul] == "white":
                l_coord_noire.append([x,y,c])
            rect(x,y,c,lcoul[indcoul])
            x += c
        y += c
                
def blanc_noire():
    global ind_noire
    rect(l_coord_noire[ind_noire][0],l_coord_noire[ind_noire][1],l_coord_noire[ind_noire][2],"black")
    ind_noire += 1
    if (ind_noire == len(l_coord_noire)):
        ind_noire = 0
        
    
    

lcoul = ["blue","white"]
root = Tk()
global ind_noire
ind_noire = 0
l_coord_noire = []

can1 = Canvas(root,bg="gray", width = 500, height = 500)
can1.pack()

b1 = Button(root,text = "damier", command = blanc_noire)
b1.pack(side = LEFT)

b2 = Button(root, text = "pions", command = blanc_noire)
b2.pack(side = RIGHT)

dam(50)




root.mainloop()


