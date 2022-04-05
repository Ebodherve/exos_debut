from random import randint
from time import time

nbm = int(input("nombre de maximal : "))

db = time()
nerr = 0 

for i in range(10) :
    a = randint(2,nbm)
    b = randint(2,nbm)
    c = a*b
    bonrep = True

    while bonrep :
        print(a," x ",b," = ",end = "")
        if c == int(input()) : 
            bonrep = False
        else :
            print("Mauvaise réponse réessayer : ")
            nerr += 1
 
fn = time()

print("nombre d'érreur : ",nerr, "temps mis : ",(fn-db),"s")

