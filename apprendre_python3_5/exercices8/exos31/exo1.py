from tkinter import *
import math


#opposite vector
def oposite(vect) :
    return [-vect[0],-vect[1]]

#the elements of speed 
def ele_speed(speed):
    return dp,dp/speed

#create vector with two point
def vect_tpoint(p1,p2) :
    return [p2[0]-p1[0],p2[1]-p1[1]]

#module of of vector
def distance_vect(vect):
    return math.sqrt(vect[0]**2+vect[1]**2)

#give module dp at one vector
def change_mod(vect) :
    d = distance_vect(vect)
    d = dp/d
    return [(d*vect[0]),(d*vect[1])]

#give for default module dp at all vector
def change_mod_d() :
    global vector_d1,vector_d2,vector_d3,vector_d4
    vector_d1 = change_mod(vector_d1)
    vector_d2 = change_mod(vector_d2)
    vector_d3 = change_mod(vector_d3)
    vector_d4 = change_mod(vector_d4)

#sum of vectors
def sum_vect(vect1,vect2):
    return [vect1[0]+vect2[0],vect1[1]+vect2[1]]

#distance point
def dist_point(p1,p2):
    return distance_vect(vect_tpoint(p1,p2))

#collision between two oval
def colision_oval(c1,c2,dist) :
    if dist_point(c1,c2) < dist:
        return True
    return False

#move of ovals 
def move_oval():
    global x1,y1,wob1,vector_d1
    x1,y1 = x1+vector_d1[0],y1+vector_d1[1]
    space.coords(ov1,x1-wob1,y1-wob1,x1+wob1,y1+wob1)
    global x2,y2,wob2,vector_d2
    x2,y2 = x2+vector_d2[0],y2+vector_d2[1]
    space.coords(ov2,x2-wob2,y2-wob2,x2+wob2,y2+wob2)
    global x3,y3,wob3,vector_d3
    x3,y3 = x3+vector_d3[0],y3+vector_d3[1]
    space.coords(ov3,x3-wob3,y3-wob3,x3+wob3,y3+wob3)
    global x4,y4,wob4,vector_d4
    x4,y4 = x4+vector_d4[0],y4+vector_d4[1]
    space.coords(ov4,x4-wob4,y4-wob4,x4+wob4,y4+wob4)

#fonctions of colisions
def colision_ov1_bor():
    global hs,ws,x1,y1,wob1,vector_d1
    if x1>ws-wob1-mm :
        if y1>hs-wob1-mm:
            x1=ws-wob1-mm
            y1=hs-wob1-mm
            vector_d1 = oposite(vector_d1)
        elif y1<wob1+mm:
            x1=ws-wob1-mm
            y1=wob1+mm
            vector_d1 = oposite(vector_d1)
        else :
            x1=ws-wob1-mm
            vector_d1 = oposite(vector_d1)
    if y1>hs-wob1-mm:
        y1=hs-wob1-mm
        vector_d1 = oposite(vector_d1)
    if x1<wob1+mm:
        if y1>hs-wob1-mm:
            x1=wob1+mm
            y1=hs-wob1-mm
            vector_d1 = oposite(vector_d1)
        elif y1<wob1+mm:
            x1=wob1+mm
            y1=wob1+mm
            vector_d1 = oposite(vector_d1)
        else :
            x1=wob1+mm
            vector_d1 = oposite(vector_d1)
    if y1<wob1+mm:
        y1=wob1+mm
        vector_d1 = oposite(vector_d1)

def colision_ov2_bor():
    global hs,ws,x2,y2,wob2,vector_d2
    if x2>ws-wob2-mm :
        if y2>hs-wob2-mm:
            x2=ws-wob2-mm
            y2=hs-wob2-mm
            vector_d2 = oposite(vector_d2)
        elif y2<wob2+mm:
            x2=ws-wob2-mm
            y2=wob2+mm
            vector_d2 = oposite(vector_d2)
        else :
            x2=ws-wob2-mm
            vector_d2 = oposite(vector_d2)
    if y2>hs-wob2-mm:
        y2=hs-wob2-mm
        vector_d2 = oposite(vector_d2)
    if x2<wob2+mm:
        if y2>hs-wob2-mm:
            x2=wob2+mm
            y2=hs-wob2-mm
            vector_d2 = oposite(vector_d2)
        elif y2<wob2+mm:
            x2=wob2+mm
            y2=wob2+mm
            vector_d2 = oposite(vector_d2)
        else :
            x2=wob2+mm
            vector_d2 = oposite(vector_d2)
    if y2<wob2+mm:
        y2=wob2+mm
        vector_d2 = oposite(vector_d2)
    
def colision_ov3_bor():
    global hs,ws,x3,y3,wob3,vector_d3
    if x3>ws-wob3-mm :
        if y3>hs-wob3-mm:
            x3=ws-wob3-mm
            y3=hs-wob3-mm
            vector_d3 = oposite(vector_d3)
        elif y3<wob3+mm:
            x3=ws-wob3-mm
            y3=wob3+mm
            vector_d3 = oposite(vector_d3)
        else :
            x3=ws-wob3-mm
            vector_d3 = oposite(vector_d3)
    if y3>hs-wob3-mm:
        y3=hs-wob3-mm
        vector_d3 = oposite(vector_d3)
    if x3<wob3+mm:
        if y3>hs-wob3-mm:
            x3=wob3+mm
            y3=hs-wob3-mm
            vector_d3 = oposite(vector_d3)
        elif y3<wob3+mm:
            x3=wob3+mm
            y3=wob3+mm
            vector_d3 = oposite(vector_d3)
        else :
            x3=wob3+mm
            vector_d3 = oposite(vector_d3)
    if y3<wob3+mm:
        y3=wob3+mm
        vector_d3 = oposite(vector_d3)

def colision_ov4_bor():
    global hs,ws,x4,y4,wob4,vector_d4
    if x4>ws-wob4-mm :
        if y4>hs-wob4-mm:
            x4=ws-wob4-mm
            y4=hs-wob4-mm
            vector_d4 = oposite(vector_d4)
        elif y4<wob4+mm:
            x4=ws-wob4-mm
            y4=wob4+mm
            vector_d4 = oposite(vector_d4)
        else :
            x4=ws-wob4-mm
            vector_d4 = oposite(vector_d4)
    if y4>hs-wob4-mm:
        y4=hs-wob4-mm
        vector_d4 = oposite(vector_d4)
    if x4<wob4+mm:
        if y4>hs-wob4-mm:
            x4=wob4+mm
            y4=hs-wob4-mm
            vector_d4 = oposite(vector_d4)
        elif y4<wob4+mm:
            x4=wob4+mm
            y4=wob4+mm
            vector_d4 = oposite(vector_d4)
        else :
            x4=wob4+mm
            vector_d4 = oposite(vector_d4)
    if y4<wob4+mm:
        y4=wob4+mm
        vector_d4 = oposite(vector_d4)

def collision_ov1234():
    global dp
    global x1,y1,wob1,vector_d1
    global x2,y2,wob2,vector_d2
    global x3,y3,wob3,vector_d3
    global x4,y4,wob4,vector_d4
    if(colision_oval([x1,y1],[x2,y2],wob1+wob2)) :
        dp = 30
        vector_d1 = change_mod(sum_vect(change_mod(vect_tpoint([x1,y1],[x2,y2])),oposite(change_mod(vector_d1))))
        vector_d2 = oposite(vector_d1)
#        vector_d2 = change_mod(sum_vect(change_mod(vect_tpoint([x2,y2],[x1,y1])),oposite(change_mod(vector_d2))))
        move_oval()
        dp = 0.1
        change_mod_d()
    if(colision_oval([x1,y1],[x3,y3],wob1+wob3)) :
        dp = 30
        vector_d1 = change_mod(sum_vect(change_mod(vect_tpoint([x1,y1],[x3,y3])),oposite(change_mod(vector_d1))))
        vector_d3 = oposite(vector_d1)
#        vector_d3 = change_mod(sum_vect(change_mod(vect_tpoint([x3,y3],[x1,y1])),oposite(change_mod(vector_d3))))
        move_oval()
        dp = 0.1
        change_mod_d()
    if(colision_oval([x1,y1],[x4,y4],wob1+wob4)) :
        dp = 30
        vector_d1 = change_mod(sum_vect(change_mod(vect_tpoint([x1,y1],[x4,y4])),oposite(change_mod(vector_d1))))
        vector_d4 = oposite(vector_d1)
#        vector_d4 = change_mod(sum_vect(change_mod(vect_tpoint([x4,y4],[x1,y1])),oposite(change_mod(vector_d4))))
        move_oval()
        dp = 0.1
        change_mod_d()
    if(colision_oval([x2,y2],[x3,y3],wob2+wob3)) :
        dp = 30
        vector_d2 = change_mod(sum_vect(change_mod(vect_tpoint([x2,y2],[x3,y3])),oposite(change_mod(vector_d2))))
        vector_d3 = oposite(vector_d2)
#        vector_d3 = change_mod(sum_vect(change_mod(vect_tpoint([x3,y3],[x2,y2])),oposite(change_mod(vector_d3))))
        move_oval()
        dp = 0.1
        change_mod_d()
    if(colision_oval([x2,y2],[x4,y4],wob2+wob4)) :
        dp = 30
        vector_d2 = change_mod(sum_vect(change_mod(vect_tpoint([x2,y2],[x4,y4])),oposite(change_mod(vector_d2))))
        vector_d4 = oposite(vector_d2)
#        vector_d4 = change_mod(sum_vect(change_mod(vect_tpoint([x4,y4],[x2,y2])),oposite(change_mod(vector_d4))))
        move_oval()
        dp = 0.1
        change_mod_d()
    if(colision_oval([x3,y3],[x4,y4],wob3+wob4)) :
        dp = 30
        vector_d3 = change_mod(sum_vect(change_mod(vect_tpoint([x3,y3],[x4,y4])),oposite(change_mod(vector_d3))))
        vector_d4 = oposite(vector_d3)
#        vector_d4 = change_mod(sum_vect(change_mod(vect_tpoint([x4,y4],[x3,y3])),oposite(change_mod(vector_d4))))
        move_oval()
        dp = 0.1
        change_mod_d()


#main focntion of deplacement
def deplacement():
    global nbclick,nbgp,nbclickmax
    move_oval()
    colision_ov1_bor()
    colision_ov2_bor()
    colision_ov3_bor()
    colision_ov4_bor()
    collision_ov1234()
    if nbclick < nbclickmax:
        root.after(1,deplacement)
    else :
        Label(root,text = " {} saisis sur {} ".format(nbgp,nbclickmax),width = 20,height = 15).grid(row = 35)

#fonction that permite to start
def start():
    global speed,vector_d1,vector_d2,vector_d3,vector_d4,dp
    vector_d1,vector_d2 = change_mod(vector_d1),change_mod(vector_d2)
    vector_d3,vector_d4 = change_mod(vector_d3),change_mod(vector_d4)
    dp = 1
    deplacement()

def trap_b(event):
    global x1,y1,wob1
    global x2,y2,wob2
    global x3,y3,wob3
    global x4,y4,wob4
    global nbclick,nbgp
    x,y = event.x,event.y
    if colision_oval([x1,y1],[x,y],wob1) :
        nbgp += 1
        nbclick += 1
    elif colision_oval([x2,y2],[x,y],wob2) :
        nbgp -= 1
        nbclick += 1
    elif colision_oval([x3,y3],[x,y],wob3) :
        nbgp -= 1
        nbclick += 1
    elif colision_oval([x4,y4],[x,y],wob4) :
        nbgp -= 1
        nbclick += 1
    else :
        nbclick += 1
    

#gui
root = Tk()

#canvas
ws = hs = 800
space = Canvas(root,width = ws,height = hs)

space.bind("<Button-1>",trap_b)

#button to start deplacement
b1 = Button(root,bg = "gray",text="start",command = start)

#data of player
global nbclick,nbgp,nbclickmax
nbclick,nbgp,nbclickmax = 0,0,15

#deplacement and minimum margin
global tu,dp
dp = 0.1    #dp = unit distance
mm = 20

#oval - 1
global x1,y1,wob1,vector_d1,spped1
wob1 = 20
x1,y1,vector_d1,spped1 = ws-wob1-mm,hs-wob1-mm,[-1,-1],4
ov1 = space.create_oval(x1-wob1,y1-wob1,x1+wob1,y1+wob1,fill = "red")

#oval - 2
global x2,y2,wob2,vector_d2,spped2
wob2 = 20
x2,y2,vector_d2,spped2 = ws-wob2-mm,wob2+mm,[-2,1],4
ov2 = space.create_oval(x2-wob2,y2-wob2,x2+wob2,y2+wob2,fill = "blue")

#oval - 3
global x3,y3,wob3,vector_d3,spped3
wob3 = 20
x3,y3,vector_d3,spped3 = wob3+mm,hs-wob3-mm,[2,-1],2
ov3 = space.create_oval(x3-wob3,y3-wob3,x3+wob3,y3+wob3,fill = "orange")

#oval - 4
global x4,y4,wob4,vector_d4,spped4
wob4 = 20
x4,y4,vector_d4,spped4 = wob4+mm,wob4+mm,[-2,-1],4.5
ov4 = space.create_oval(x4-wob4,y4-wob4,x4+wob4,y4+wob4,fill = "green")



#adaptation of space and button
space.grid(rowspan = 50)
b1.grid(row = 51)


#start of gui
root.mainloop()
