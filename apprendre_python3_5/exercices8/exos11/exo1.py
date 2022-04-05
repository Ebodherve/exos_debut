

from tkinter import *


def cercle(x,y,r):
    canvas1.create_oval(x-r,y-r,x+r,y+r,fill = "red")


def cercle_clic(event):
    cercle(event.x,event.y,5)


root = Tk()
canvas1 = Canvas(root,bg = "light blue",width = 500,height = 800)
canvas1.bind("<Button-1>",cercle_clic)
canvas1.pack()
root.mainloop()


