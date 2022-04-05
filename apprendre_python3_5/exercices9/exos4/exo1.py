from os import chdir

chdir("/home/tsanga/Bureau/CONSERVE/conserve2/programmation/apprentissage/python/apprendre_python3_5/exercices9/exos4")

def copy_fich(fich1 = "fichtext1.txt"):
    f1 = open(fich1,'r')
    lignes1 = f1.readlines()
    lignes2 = []
    
    for l in lignes1 :
        l2 = ""
        for car in l:
            if car == " ":
                l2 += "   "
            else:
                l2 += car
        lignes2.append(l2)
    f1.close()
    f1 = open("fich_copy.txt","a")
    for l in lignes2 :
        f1.write(l)
            
    
copy_fich()    



