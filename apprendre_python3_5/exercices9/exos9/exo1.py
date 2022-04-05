from os import chdir

chdir("/home/tsanga/Bureau/CONSERVE/conserve2/programmation/apprentissage/python/apprendre_python3_5/exercices9/exos9")

def ajout_info(fich_info = "club"):
    anfich = open(fich_info,"r")
    nvfich = open("nvinfo","a")
    
    lignes1 = anfich.readlines()
    lignes2 = []
    print("entrer des informations supplémentaires : ")
    for i in range(0,len(lignes1), 6) :
        for j in range(i,i+5):
            lignes2.append(lignes1[j])
            print(lignes1[j])
        lignes2.append(input("date de naissance : ")+"\n")
        lignes2.append(input("sexe : ")+"\n")
    for ligne in lignes2:
        nvfich.write(ligne)
    nvfich.close()
    
ajout_info(fich_info = "club")
