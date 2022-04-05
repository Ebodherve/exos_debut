from dessins_tortue import *
from turtle import *

up()
goto(-300, 50)
# relever le crayon
# reculer en haut à gauche
# dessiner dix carrés rouges, alignés :

"""i = 0
dim = 11
while i < 10:
    down()    # abaisser le crayon
    carre(100/(dim-i),'red',90)      # tracer un carré
    up()
    forward(40)
    i = i +1
    down()
    triangle(100/(dim-i),'green',120) # tracer un carré
    up()    # relever le crayon
    forward(40)    # avancer + loin
    i+=1
"""
i = 0
dim = 6
ecart = 10

while i < 5:
    down()    # abaisser le crayon
    distance = 80/(dim-i)
    etoile5(distance,'blue',144)      # tracer un carré
    up()
    forward(ecart+distance)
    i+=1

i=0    
dim = 2
while i < 5:
    down()    # abaisser le crayon
    distance = 80/(dim+i)
    etoile5(distance,'blue',144)      # tracer un carré
    up()
    forward(ecart+distance)
    i+=1
    

a = input()     # attendre
