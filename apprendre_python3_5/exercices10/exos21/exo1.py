
#fonction qui copie un fichier avec la form utf-8 dans un autre en mettant chaque caratere du debut en majuscule
def copie_modifie(nom_fich_cp,nom_fich_de) :
    fich_cp = open(nom_fich_cp,mode="r",encoding="Utf-8")
    fich_de = open(nom_fich_de,mode="w",encoding="Utf-8")
    liste_lignes_cp = fich_cp.readlines()
    for ligne in liste_lignes_cp:
        fich_de.write(ligne.capitalize())
    fich_de.close()
    fich_cp.close()

fich_copie = input("Nom du fichier à copier : ")
fich_destination = input("Nom du fichier de destination :")

fich_copie = "exercices10/exos21/"+fich_copie
fich_destination = "exercices10/exos21/"+fich_destination

copie_modifie(fich_copie,fich_destination)

