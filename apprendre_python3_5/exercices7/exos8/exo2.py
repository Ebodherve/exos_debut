from dessins_tortue import *

up()
goto(-75, 20)


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

for i in range(4) :
    carre(dim,coulca,90)
    up()
    forward(dim+ecart)
    down()
    etoile6(dim/3,coulet,60)
    up()
    forward(2*dim/3 + ecart)
    down()
    dim = taille - (i+1)*4




"""right(-120)
forward(20)
"""

input()


