from tkinter import *
import math as m

#calcul of distance between two points
def distance_between(p1,p2):
    return m.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

#place oval at one place
def place():
    global x2,y2,wa2
    global x3,y3,wa3
    space.coords(ast2,x2-wa2,y2-wa2,x2+wa2,y2+wa2)
    space.coords(ast3,x3-wa3,y3-wa3,x3+wa3,y3+wa3)

#fonction to turn astres
def turn():
    global x1,y1
    global x2,y2,wa2,angle2,d2,da2
    global x3,y3,wa3,angle3,d3,da3
    
    x2,y2 = x1+d2*m.cos(angle2),y1+d2*m.sin(angle2)
    x3,y3 = x1+d3*m.cos(angle3),y1+d3*m.sin(angle3)
    place()
    angle2 += da2
    angle3 += da3


#fonction for ratation of astre
def rotation():
    turn()
    root.after(100,rotation)

#begin the movement
def star():
    rotation()

#main window
root = Tk()

#space of movements
ws = hs = 800
space = Canvas(root,width = ws,height = hs,bg = "light gray")

#astre1 - stars
global x1,y1,wa1
x1,y1,wa1 = hs/2,ws/2,50
ast1 = space.create_oval(x1-wa1,y1-wa1,x1+wa1,y1+wa1,fill = "light blue")

#astre3 - planet
global x2,y2,wa2,angle2,d2,da2
x2,y2,wa2,angle2 = x1+200,y1,15,0
ast2 = space.create_oval(x2-wa2,y2-wa2,x2+wa2,y2+wa2,fill = "green")
d2 = distance_between([x1,y1],[x2,y2])
da2 = 0.1

#astre4 - planet
global x3,y3,wa3,angle3,d3,da3
x3,y3,wa3,angle3 = x1+300,y1,20,0
ast3 = space.create_oval(x3-wa3,y3-wa3,x3+wa3,y3+wa3,fill = "beige")
d3 = distance_between([x1,y1],[x3,y3])
da3 = 0.15

rotation()

#adaptation of space
space.grid()

#start of gui
root.mainloop()
