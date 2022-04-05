

# Jeu de Juniper-Green

from random import randint

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

def copie_l() :
    part2[:] = []
    for e in part1 :
        part2.append(e)


Nmax = 50
nbparties = 500
part1 = []
part2 = []

# Début du jeu

print("Je joue ",nbparties," parties entre 1 et",Nmax)
#print("Je choisis comme nombre de départ",mon_nombre)



for i in range(nbparties) :
    possibles = list(range(1,Nmax+1))       # liste des nombres pas encore utilisés
    mon_nombre=2*randint(1,Nmax/2)          #l'ordinateur choisit un nombre pair
    possibles.remove(mon_nombre)            #on enlèvera de la liste "possibles" tous les
    valides = diviseurs(mon_nombre) + multiples(mon_nombre)

    while valides != []:
        print("Nombres valides:",valides)
        ton_nombre = valides[randint(0,len(valides)-1)]
        part1.append(ton_nombre)
        while ton_nombre not in valides:
            ton_nombre = int(input("Incorrect. Que jouez-vous ? "))
            
        possibles.remove(ton_nombre)
        valides = diviseurs(ton_nombre) + multiples(ton_nombre)
        if valides == []:
            print("Bravo!")
        else:
            mon_nombre = valides[randint(0,len(valides)-1)]
            part1.append(mon_nombre)
            print("Nombres valides :",valides)
            print("Je joue",mon_nombre)
            possibles.remove(mon_nombre)
            valides = diviseurs(mon_nombre) + multiples(mon_nombre) 
            if valides == []:
                print("Vous avez perdu!")
    if len(part1) > len(part2) :
        copie_l()
    part1[:] = []

print("plus longue partie : ",len(part2),"coups")
print(part2)        



