from random import randint

nbm = int(input("nombre de maximal : "))


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



