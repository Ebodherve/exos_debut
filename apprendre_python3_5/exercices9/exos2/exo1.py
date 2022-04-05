from os import chdir

chdir("/home/tsanga/Bureau/CONSERVE/conserve2/programmation/apprentissage/python/apprendre_python3_5/exercices9/exos2")

def plus_longue(nfich):
    fich = open(nfich,"r")
    lines = fich.readlines()
    lignel = lines[0]
    for ligne in lines[1:] :
        if(len(ligne)>len(lignel)) :
            lignel = ligne
    fich.close()
    return lignel


print("la plus longue ligne de ce fichier est :")
print(plus_longue("fiche"))    


