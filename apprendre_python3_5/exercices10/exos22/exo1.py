
#copie et collage des informations d'un fichier dans un autre
from os import link


def copie_colle(nom_fich_cp,nom_fich_de):
    fich_cp = open(nom_fich_cp,mode = "rb")
    fich_de = open(nom_fich_de,mode = "wb")
    
    for ligne in fich_cp.readlines():
        fich_de.write(b"-*-".join(ligne.split(b" ")))
    
    fich_de.close()
    fich_cp.close()


fich_cp = "exercices10/exos22/"+input('nom du fichier à copier : ')
fich_de = "exercices10/exos22/"+input("nom du fichier de destination :")

copie_colle(fich_cp,fich_de)
