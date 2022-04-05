from dessins_tortue import *

up()
goto(10, 250)


#etoile6(10,"blue",60)

taille = 50
dim = taille
coulet = "blue"
coulca = "red"
ecart = 30

down()
carre(dim,coulca,90)
up()
forward(dim+ecart)
down()
etoile6(dim/3,coulet,60)
up()
forward(2*dim/3 + ecart)
down()

for i in range(8) :
    triangle(dim,coulca,120)
    up()
    forward(dim+ecart)
    down()
    etoile5(dim,coulet,144)
    up()
    forward(dim+ecart)
    down()
    carre(dim,coulca,90)
    up()
    forward(dim+ecart)
    down()
    etoile6(dim/3,coulet,60)
    up()
    forward(2*dim/3 + ecart)
    down()
    dim = taille - (i+1)*4

triangle(dim,coulca,120)
up()
forward(dim+ecart)
down()
etoile5(dim,coulet,144)


"""right(-120)
forward(20)
"""

input()

