"""ce programme consite à en un jeu de lequelle le joueur doit cliquer sur une balle en plein déplacement
pour obtenir un point """

from tkinter import *
import math

#function to give one distance at vector_d
def distance_vect(dist) :
    global vector_d
    d_vect = math.sqrt(vector_d[0]**2 + vector_d[1]**2)
    vector_d = [vector_d[0]*dist/d_vect, vector_d[1]*dist/d_vect]

#function of change direction
def change_direction() :
    global vector_d,directions,etat
    d_vect = math.sqrt(vector_d[0]**2 + vector_d[1]**2)
    vector_d = [-vector_d[0],-vector_d[1]]
    ang = directions[(etat)%len(directions)]
    vector_d = [vector_d[0]*math.cos(ang),vector_d[1]*math.sin(ang)]
    distance_vect(10)
    if vector_d[0]**2/vector_d[1]**2 < 0.2 :
        vector_d[0] += 10*(vector_d[0])
    elif vector_d[1]**2/vector_d[0]**2 < 0.2 :
        vector_d[1] += 10*(vector_d[1])
    else :
        pass
    etat += 1

#function to put object at one place
def move() :
    global xob,yob,wob,vector_d,col
    xob,yob = xob+vector_d[0], yob+vector_d[1]
    space.delete(ALL)
    space.create_oval(xob-wob,yob-wob,xob+wob,yob+wob,fill = col)

#function of game
def play_game() :
    global xob,yob,wob,score,maxclick,nbclick,game,vector_d
    d = 20
    bstart.configure(text = "start"+str(etat))
    if game :
        if xob < wob+d :
            xob = wob+d
            change_direction()
            move()
        if xob > ws-wob-d :
            xob = ws-wob-d-1
            change_direction()
            move()
        if yob < wob+d :
            yob = wob+d
            change_direction()
            move()
        if yob > ws-wob-d :
            yob = ws-wob-d-20
            change_direction()
            move()
        else :
            move()
        if nbclick < maxclick :
            root.after(100,play_game)
        else:
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
    global xob,yob,wob,score,nbclick,dist_im,indcol,col,colors
    if distance_tp(xob,yob,event.x,event.y) < wob :
        wob -= 0.5
        score += 1
        col = colors[indcol%len(colors)]
        indcol += 1
    nbclick += 1

#creation of window
root = Tk()

#creation of space of game
ws,hs = 800,800
space = Canvas(root,width = hs,height = hs,bg = "grey")
space.bind("<Button-1>",click)

#object which deplace himself and his properties
global xob,yob,wob
xob,yob,wob = 20,20,20
objd = space.create_oval(xob-wob,yob-wob,xob+wob,yob+wob,fill = "orange")

#vector and one variable wich permit to game  
global game,vector_d
game = False
vector_d = [10,15]

#element of play like score
global score,maxclick,nbclick,directions,etat,colors,indcol,col
score,maxclick,nbclick,etat,indcol = 0,15,0,0,0
#directions = [0.5,-1,-0.5,2,-2,0.75,-0.75,1,0.9]
directions = [0.5,0.7,0.9,1.1,2,3,4]
#liste of color
colors = ["light yellow","white","light green","light blue","orange","blue","red","green","yellow","beige"]
#button to start
bstart = Button(root,text = 'start',command = start)
#color
col = "beige"

#button to quit the window
bq = Button(root,text = "quitter",bg = "gray",command = root.quit)

#label to affiche the score
lab = Label(root,bg = "brown",height = 10)

#adaptation space and others widgets
space.grid(rowspan = 50,columnspan = 20)
bstart.grid(row = 51,column = 1)
bq.grid(row = 51,column = 2)

#start()
#start of gui
root.mainloop()


