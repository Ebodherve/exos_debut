"""ce programme consite à en un jeu de lequelle le joueur doit cliquer sur une balle en plein déplacement
pour obtenir un point """

from tkinter import *
import math

#function to put object at one place
def move() :
    global xob,yob,wob,vector_d,coul,score
    xob,yob = xob+vector_d[0], yob+vector_d[1]
    space.delete(ALL)
    space.create_oval(xob-wob,yob-wob,xob+wob,yob+wob,fill = coul[score%len(coul)])

#function to game
def play_game() :
    global xob,yob,wob,score,maxclick,nbclick,game,direction,it,vector_d
    d = 20
    if game :
        if xob < wob+d and yob < wob +d :
            xob,yob = wob+d,wob+d
            vector_d = [10,10]
            move()
        elif xob > ws-wob-d and yob > hs-wob-d :
            xob,yob = ws-wob-d-1,hs-wob
            vector_d = [0,-10]
            move()
        elif xob > ws-wob-d*2 and yob < wob+d :
            xob,yob = ws-wob-d,wob+d
            vector_d = [-10,10]
            move()
        elif xob < wob+d and yob > ws-wob-d :
            xob,yob = wob,ws-wob-d
            vector_d = [0,-10]
            move()
        else :
            move()
        if nbclick < maxclick :
            root.after(50,play_game)
        else:
            game = False
            lab.configure(text = "score : {} clique bien placés sur {} ".format(score,nbclick))
            lab.grid(row = 25)
        
#function to start game
def start():
    global game
    game = True
    play_game()

#distance between two point
def distance_tp(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


#function to control the podition of click
def click(event) :
    global xob,yob,wob,score,nbclick,dist_im,wob
    if distance_tp(xob,yob,event.x,event.y) < wob :
        score += 1
        wob -=1
    nbclick += 1

#creation of window
root = Tk()

#creation of space of game
ws,hs = 800,800
space = Canvas(root,width = hs,height = hs)
space.bind("<Button-1>",click)

#object which deplace himself and his properties
global xob,yob,wob
xob,yob,wob = 20,20,20
objd = space.create_oval(xob-wob,yob-wob,xob+wob,yob+wob,fill = "orange")

#vector and one variable wich permit to game  
global game,vector_d,coul
coul = ["orange","blue","red","green","orange","cyan"]
game = False
vector_d = [10,10]

#element of play like score
global score,maxclick,nbclick
score,maxclick,nbclick = 0,10,0

#button to start
bstart = Button(root,text = 'start',command = start)

#button to quit the window
bq = Button(root,text = "quitter",bg = "gray",command = root.quit)

#label to affiche the score
lab = Label(root,bg = "brown",height = 10)

#adaptation space and others widgets
space.grid(rowspan = 50,columnspan = 20)
bstart.grid(row = 51,column = 1)
bq.grid(row = 51,column = 50) 

#start()
#start of gui
root.mainloop()



