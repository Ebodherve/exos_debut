from random import randint, choice
from time import time

operateur = ["*","/","+","-"]
op = choice(operateur)

if op == "*" :
    nbm = int(input("nombre de maximal pour effectuer la multiplication: "))
elif op == "/" :
    nbm = int(input("nombre de maximal pour effectuer la division entière: "))
elif op == "+" :
    nbm = int(input("nombre de maximal pour effectuer la somme: "))
else:
    nbm = int(input("nombre de maximal pour effectuer la soustraction: "))



db = time()
nerr = 0 

for i in range(10) :
    a = randint(2,nbm)
    b = randint(2,nbm)
    if op == "*" :
        c = a*b
    elif op == "/" :
        c = a//b 
    elif op == "+" :
        c = a+b
    else :
        c = a-b

    
    bonrep = True

    while bonrep :
        print(a," ",op," ",b," = ",end = "")
        if c == int(input()) : 
            bonrep = False
        else :
            print("Mauvaise réponse réessayer : ")
            nerr += 1
 
fn = time()

print("nombre d'érreur : ",nerr, "temps mis : ",(fn-db),"s")



