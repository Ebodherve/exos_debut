from tkinter import *
from random import choice

fen = Tk()


limage = PhotoImage(file = "pierre.gif"),PhotoImage(file = "papier.gif"),PhotoImage(file = "ciseaux.gif")


for i in range(6) :
    b = Button(fen)
    b.grid(row = 0, column = i)
    b.configure(image = choice(limage))

for i in range(6) :
    b = Button(fen)
    b.grid(row = 1, column = i)
    b.configure(image = choice(limage))

fen.mainloop()

