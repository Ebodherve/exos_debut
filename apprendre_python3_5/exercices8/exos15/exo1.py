

from tkinter import *
import math  


#calcule la distance entre les duex astres
def distance():
    return math.sqrt((x1-x2)**2+(y1-y2)**2),math.sqrt((x2-x3)**2+(y2-y3)**2),math.sqrt((x1-x3)**2+(y1-y3)**2) 

#definition d'une fonction de calcule d'une valeur absolue
def val_ab(nbr) :
    if nbr<0:
        return -1*nbr
    return nbr

#création d'un vecteur à partir de point
def vecteur(p1,p2) :
    return [p2[0]-p1[0],p2[1]-p1[1]]

#longueur d'un vecteur
def longueur_vect(v):
    return math.sqrt(v[0]**2+v[1]**2)

#définition du vecteur unitaire d'un vecteur
def  vect_unit(v):
    longueur = longueur_vect(v)
    return [v[0]/longueur,v[1]/longueur]

#multiplication d'un vecteur par un scalaire
def mult_vs(v,s) :
    return [s*v[0],s*v[1]]   

#somme de duex vecteurs
def somme_vect(v1,v2):
    return [v1[0]+v2[0],v1[1]+v2[1]]

#définition du sens d'un vecteur force élèctrique en fonction du signe des charges
def sens_vectele(s1,s2):
    return -1*s1*s2


#deplacement d'un astre
def deplace_ast(event):
    global choix_ast,x1,y1,x2,y2,x3,y3,r1,r2,r3
    if  choix_ast == 0 :
        x1 = event.x
        y1 = event.y
        can.coords(ast1,x1-r1,y1-r1,x1+r1,y1+r1)
        dist = distance()
        forces = force_atract()
        labd1.configure(text = "distance entre les charges élèctriques bleu et orange : "+str(dist[0]))
        labd2.configure(text = "distance entre les charges élèctriques bleu et vert : "+str(dist[1]))
        labd3.configure(text = "distance entre les charges élèctriques orange et vert : "+str(dist[2]))
        labf1.configure(text = "force d'attraction sur la charge élèctrique orange : "+str(forces[0]))
        labf2.configure(text = "force d'attraction sur la charge élèctrique bleu : "+str(forces[1]))
        labf3.configure(text = "force d'attraction sur la charge élèctrique verte : "+str(forces[2]))
    elif choix_ast == 1:
        x2 = event.x
        y2 = event.y
        can.coords(ast2,x2-r2,y2-r2,x2+r2,y2+r2)
        dist = distance()
        forces = force_atract()
        labd1.configure(text = "distance entre les charges élèctriques blues et oranges : "+str(dist[0]))
        labd2.configure(text = "distance entre les charges élèctriques blues et rouges : "+str(dist[1]))
        labd3.configure(text = "distance entre les charges élèctriques blues et verts : "+str(dist[2]))
        labf1.configure(text = "force d'attraction sur la charge élèctrique orange : "+str(forces[0]))
        labf2.configure(text = "force d'attraction sur la charge élèctrique bleu : "+str(forces[1]))
        labf3.configure(text = "force d'attraction sur la charge élèctrique verte : "+str(forces[2]))
    else :
        x3 = event.x
        y3 = event.y
        can.coords(ast3,x3-r3,y3-r3,x3+r3,y3+r3)
        dist = distance()
        forces = force_atract()
        labd1.configure(text = "distance entre les charges élèctriques blues et oranges : "+str(dist[0]))
        labd2.configure(text = "distance entre les charges élèctriques blues et rouges : "+str(dist[1]))
        labd3.configure(text = "distance entre les charges élèctriques blues et verts : "+str(dist[2]))
        labf1.configure(text = "force d'attraction sur la charge élèctrique orange : "+str(forces[0]))
        labf2.configure(text = "force d'attraction sur la charge élèctrique bleu : "+str(forces[1]))
        labf3.configure(text = "force d'attraction sur la charge élèctrique verte: "+str(forces[2]))    


#calcul de la resultante des forces chacun des trois astres 
def force_atract():
    global G,m1,m2,x1,y1,x2,y2,x3,y3,s1,s2,s3
    dist = distance()
    f12 = G*m1*m2/(dist[0])**2
    f23 = G*m2*m3/(dist[1])**2
    f13 = G*m1*m3/(dist[2])**2
    #resultante des forces sur la charge 1
    vf12 = mult_vs(vect_unit(vecteur([x1,y1],[x2,y2])),f12*sens_vectele(s1,s2))
    vf13 = mult_vs(vect_unit(vecteur([x1,y1],[x3,y3])),f13*sens_vectele(s1,s3))
    f1 = longueur_vect(somme_vect(vf12,vf13))
    #resultante des forces sur la charge 2
    vf21 = mult_vs(vect_unit(vecteur([x2,y2],[x1,y1])),f12*sens_vectele(s1,s2))
    vf23 = mult_vs(vect_unit(vecteur([x2,y2],[x3,y3])),f23*sens_vectele(s2,s3))
    f2 = longueur_vect(somme_vect(vf21,vf23))
    #resultante des forces sur la charge 3
    vf31 = mult_vs(vect_unit(vecteur([x3,y3],[x1,y1])),f13*sens_vectele(s1,s3))
    vf32 = mult_vs(vect_unit(vecteur([x3,y3],[x2,y2])),f23*sens_vectele(s2,s3))
    f3 = longueur_vect(somme_vect(vf31,vf32))
    
    return f1,f2,f3


def change_choice() :
    global choix_ast
    if choix_ast == 0:
        choix_ast = 1
        bc.configure(bg = "blue")
        bcs.configure(bg = "blue")
    elif choix_ast == 1:
        choix_ast = 2
        bc.configure(bg = "green")
        bcs.configure(bg = "green")
    else:
        choix_ast = 0
        bc.configure(bg = "orange")
        bcs.configure(bg = "orange")

#fonction permettant de changer le sicne d'une charge
def change_signe():
    global choix_ast,s1,s2,s3
    if choix_ast == 0:
        s1*=-1
    elif choix_ast == 1:
        s2*=-1
    else:
        s3*=-1
    forces = force_atract()
    labf1.configure(text = "force d'attraction sur la charge élèctrique orange : "+str(forces[0]))
    labf2.configure(text = "force d'attraction sur la charge élèctrique bleu : "+str(forces[1]))
    labf3.configure(text = "force d'attraction sur la charge élèctrique verte : "+str(forces[2]))    


#coordonnées des deux astres
global x1,y1,x2,y2,x3,y3,s1,s2,s3
x1,y1,x2,y2,x3,y3 = 50,100,400,100,300,400 
s1,s2,s3 = 1,1,1

#rayon des deux astres et masses
global r1,r2,r3,m1,m2,m3,G
r1,r2,r3,m1,m2,m3 = 10,20,15,80,90,85
G = 6.67*(10**(-11))

#choix d'un astre
global choix_ast
choix_ast = 0

#fenetre
root = Tk()

#canvas
can = Canvas(root,bg = "grey", width = 600, height = 600)

#gestion du deplacment des astres au clic de la souris
can.bind("<Button-1>",deplace_ast)

#astre 1
ast1 = can.create_oval(x1-r1,y1-r1,x1+r1,y1+r1,fill = "orange")
ast2 = can.create_oval(x2-r2,y2-r2,x2+r2,y2+r2,fill = "blue")
ast3 = can.create_oval(x3-r3,y3-r3,x3+r3,y3+r3,fill = "green")

#labels d'affichage des masses des deux boules  
lab1 = Label(root,text = "charge élèctrique orange, masse : "+str(m1),width = 75, bg = "orange")
lab2 = Label(root,text = "charge élèctrique bleu, masse : "+str(m2),width = 75, bg = "blue")
lab3 = Label(root,text = "charge élèctrique vert, masse : "+str(m3),width = 75, bg = "green")

#differentes distances
dist = distance()

#différentes résultante des forces d'attraction
res_forces = force_atract()

#labels d'affichage des distances et forces d'attraction entre les deux boulles  
labd1 = Label(root,text = "distance entre les charges élèctriques orange et bleu : "+str(dist[0]), width = 75, bg = "gray")
labd2 = Label(root,text = "distance entre les charges élèctriques bleu et vert :"+str(dist[1]), width = 75, bg = "gray")
labd3 = Label(root,text = "distance entre les charges élèctriques orange et vert :"+str(dist[2]), width = 75, bg = "gray")


labf1 = Label(root,text = "force d'attraction  : "+str(res_forces[0]), width = 75, bg = "red")
labf2 = Label(root,text = "force d'attraction  : "+str(res_forces[1]), width = 75, bg = "red")
labf3 = Label(root,text = "force d'attraction  : "+str(res_forces[2]), width = 75, bg = "red")


#boutton permettant de changer la charge courante
bc = Button(root,text = "changer de charge élèctrique",bg = "orange",command = change_choice)  

#boutton permettant de changer le signe de la charge manipulée
bcs = Button(root,text = "changer le signe de l'astre manipulée",bg = 'orange',command = change_signe) 

#boutton permettant de quitter la fenetre
bq = Button(root,text = "quitter", command = root.quit)

lab1.grid(row = 1)
lab2.grid(row = 2)
lab3.grid(row = 3)

can.grid(row = 4,rowspan = 50)

labf1.grid(row = 53,sticky = S)
labf2.grid(row = 54,sticky = S)
labf3.grid(row = 55,sticky = S)

labd1.grid(row = 56,sticky = S)
labd2.grid(row = 57,sticky = S)
labd3.grid(row = 58,sticky = S)


bc.grid(row = 5,column = 2,sticky = N)
bcs.grid(row = 6,column = 2,sticky = N)
bq.grid(row = 52,column = 2,sticky = N)

#démarrage de l'interface gaphique
root.mainloop()







