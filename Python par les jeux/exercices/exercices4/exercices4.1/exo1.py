from tkinter import *

fen = Tk()


lab1 = Label(fen, text = "0",font = ("Helvetica",40))
lab1.grid(row = 0,columnspan = 4)



global val
val = 0

def incr():
    global val
    val += 1
    lab1.configure(text = str(val))
     
def recom() :
    global val
    val = 0
    lab1.configure(text = '0')

def quite():
    fen.destroy()

bout1 = Button(fen,text = 'incrémenter',command = incr)
bout1.grid(row = 1,column = 0,rowspan = 8)

bout2 = Button(fen,text = "Recommancer",command = recom)
bout2.grid(row = 1, column = 1,rowspan = 8)

bout3 = Button(fen, text = "quitter",command = quite)
bout3.grid(row = 1, column = 2,rowspan = 8)

fen.mainloop()

