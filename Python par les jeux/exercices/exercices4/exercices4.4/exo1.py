from tkinter import *
from random import choice

fen = Tk()

lmain = []

lmain.append(PhotoImage(file = "pierre.gif"))
lmain.append(PhotoImage(file = "papier.gif"))
lmain.append(PhotoImage(file = "ciseaux.gif"))



for i in range(6) :
    b = Button(fen)
    b.grid(row = 0, column = i)
    b.configure(image = choice(lmain))

for i in range(6) :
    b = Button(fen)
    b.grid(row = 1, column = i)
    b.configure(image = choice(lmain))

fen.mainloop()

