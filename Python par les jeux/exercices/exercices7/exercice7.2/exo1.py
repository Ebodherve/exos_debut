#jeu du pendu

from random import choice,shuffle
#/home/tsanga/Bureau/CONSERVE/conserve2/programmation/apprentissage/python/Python par les jeux/exercices/exercices7/exercice7.1/mots.txt

fichier = open("/home/tsanga/Bureau/CONSERVE/conserve2/programmation/apprentissage/python/Python par les jeux/exercices/exercices7/exercice7.1/mots.txt", "r")
liste_mots = fichier.readlines()                            # met tous les mots du fichiers dans une liste
mot = choice(liste_mots)                                    # prend au hasard un mot dans la liste
mot = mot.rstrip()                                          # supprime le caractère "saut à la ligne"
mot = mot.upper()
fichier.close()

liste_carac = list(mot)
liste_carac.sort()
mot_devine = ""
for i in liste_carac :
    mot_devine += i

mot_devine = mot_devine.upper()
print(mot_devine)
nvmot = input("entrez l'anagramme : ")

nvmot = nvmot.upper()
if nvmot != mot:
    print("Vous avez perdu !")
else :
    print('Bravo !')

