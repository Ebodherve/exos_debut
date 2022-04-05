from os import chdir

chdir("/home/tsanga/Bureau/CONSERVE/conserve2/programmation/apprentissage/python/apprendre_python3_5/exercices9/exos11")

def select_pren(fich = "nvinfo") :
    fic = open(fich,"r")
    lignes = fic.readlines()
    fic.close()
    liste_n = []
    for i in range(0,len(lignes),7):
        if "F" <= lignes[i][0] and lignes[i][0] <= "M" :
           liste_n.append(lignes[i][:-1])
    return liste_n


print(select_pren())

# kueppo tcheukam joseph wesley 18T2621
# TAMO MBOBDA Eric 18T2578
