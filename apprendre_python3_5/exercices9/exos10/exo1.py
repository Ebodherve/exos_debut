from os import chdir

chdir("/home/tsanga/Bureau/CONSERVE/conserve2/programmation/apprentissage/python/apprendre_python3_5/exercices9/exos10")

def code_post(fich = "nvinfo"):
    fich1 = open(fich,"r")
    lignes = fich1.readlines()
    for i in range(0,len(lignes),7) :
        print(" {} à pour code postale {} ".format(lignes[i],lignes[i+3]))
        
code_post()

