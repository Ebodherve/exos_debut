# Jeu de Juniper-Green

from random import randint,choice

def multiples(n):
    #renvoie la liste des multiples de n <= Nmax
    mult=[] 
    i=2
    while i*n <= Nmax :
        if i*n in possibles: # on l'ajoute seulement s'il n'a pas été joué
            mult.append(i*n)
        i += 1
    return mult
    
def diviseurs(n):
    #renvoie la liste des diviseurs de n
    div = []
    i=n
    while i >= 1:
        if n%i == 0 and n//i in possibles: # on l'ajoute s'il n'a pas été joué
            div.append(n//i)
        i-=1
    return div

def jeu_o() :
    global Nmax

    mon_nombre=2*randint(1,Nmax/2)          #l'ordinateur choisit un nombre pair
    possibles.remove(mon_nombre)            #on enlèvera de la liste "possibles" tous les
                                        #nombres joués
    print("Jouons avec des nombres entre 1 et",Nmax)
    print("Je choisis comme nombre de départ",mon_nombre)

    valides = diviseurs(mon_nombre) + multiples(mon_nombre)

    while valides != []:
        print("Nombres valides:",valides)
        ton_nombre=int(input("Que jouez-vous ? "))
        while ton_nombre not in valides:
            ton_nombre=int(input("Incorrect. Que jouez-vous ? "))
            
        possibles.remove(ton_nombre)
        valides = diviseurs(ton_nombre) + multiples(ton_nombre)
        if valides == []:
            print("Bravo!")
        else:
            mon_nombre = valides[randint(0,len(valides)-1)]
            print("Nombres valides :",valides)
            print("Je joue",mon_nombre)
            possibles.remove(mon_nombre)
            valides = diviseurs(mon_nombre) + multiples(mon_nombre)
            if valides == []:
                print("Vous avez perdu!")

def jeu_u() :
    global Nmax


    #mon_nombre=2*randint(1,Nmax/2)          #l'ordinateur choisit un nombre pair
    

    print("Jouons avec des nombres entre 1 et",Nmax)
    ton_nombre=int(input("Que jouez-vous ? "))
    possibles.remove(ton_nombre)            #on enlèvera de la liste "possibles" tous les nombres joués
    
    #print("Je choisis comme nombre de départ",mon_nombre)

    valides = diviseurs(ton_nombre) + multiples(ton_nombre)
    print("Nombres valides:",valides)
    
    while valides != []:
        #print("Nombres valides:",valides)

        """minc_o = choice([1,len(possibles)//2 - 1])
        maxc_o = choice([len(possibles),len(possibles)//2])"""
        minc_o = 1
        maxc_o = 1
        ensc_o = valides+possibles[minc_o:maxc_o]
        mon_nombre = choice(ensc_o)
        print("je joue :")

        while mon_nombre not in valides:
            print(mon_nombre,"oups, j'ai raté je recommence")
            ensc_o.remove(mon_nombre)
            mon_nombre = choice(ensc_o)
        
        print(mon_nombre)

        possibles.remove(mon_nombre)
        valides = diviseurs(mon_nombre) + multiples(mon_nombre)
        print('valeurs possibles : ',possibles)
        if valides == []:
            print("Youpi, j'ai gagner !")
        else:            
            ton_nombre=int(input("Que jouez-vous ? "))
            valides = diviseurs(ton_nombre) + multiples(ton_nombre)
            print("Nombres valides :",valides)        
            if ton_nombre in possibles :
                possibles.remove(ton_nombre)
    
            valides = diviseurs(ton_nombre) + multiples(ton_nombre)
            if valides == []:
                print("j'ai perdue !")

global Nmax

# Début du jeu


Nmax = -1


while Nmax <= 2 :
    Nmax = int(input("entrer une valeur maximale superieur 2 : "))
   
possibles = list(range(1,Nmax+1))       # liste des nombres pas encore utilisés
 
if input("voulez vous entrer en premier ? (o/n)") in ['o','oui','ou','u'] :
    jeu_u()
else :
    jeu_o()




