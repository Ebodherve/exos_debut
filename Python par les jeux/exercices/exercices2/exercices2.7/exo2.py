from random import randint

nombre_lancer = 100

nombre_pile = 0
nombre_face = 0

print("lancer de la piece : ")
print("")

while nombre_lancer != 0 :
    resultat_lancer = randint(0,1)

    if resultat_lancer == 0 :
        nombre_pile += 1
    else :
        nombre_face += 1
    nombre_lancer -= 1

print("nombre de resultats pile = ",nombre_pile)
print("nombre de resultats face = ",nombre_face)




