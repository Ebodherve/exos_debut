from random import randint

nombre_pile = 0
nombre_face = 0

print("lancer de la piece : ")
print("")

for i in range(100) :
    resultat_lancer = randint(0,1)

    if resultat_lancer == 0 :
        nombre_pile += 1
    else :
        nombre_face += 1

print("nombre de resultats pile = ",nombre_pile)
print("nombre de resultats face = ",nombre_face)




