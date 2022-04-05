from os import chdir

chdir("/home/tsanga/Bureau/CONSERVE/conserve2/programmation/apprentissage/python/apprendre_python3_5/exercices9/exos5")

def arrondi_int(nfich = "fich_reel") :
    f = open(nfich,"r")
    lignes = f.readlines()
    f.close
    f2 = open("copy_entier","w")
    for ligne in lignes :
        nb = ""
        for car in ligne:
            if car != "." and car != "\n":
                nb += car
            else:
                break
        f2.write(nb+"\n")
    f2.close()
    
arrondi_int()

