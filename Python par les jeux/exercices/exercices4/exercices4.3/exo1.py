from tkinter import *

fen = Tk()

main = PhotoImage(file = "pierre.gif")


for i in range(5) :
    b = Button(fen)
    b.grid(row = 0, column = i)
    b.configure(image = main)



fen.mainloop()

