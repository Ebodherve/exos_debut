from os import chdir

chdir("/home/tsanga/Bureau/CONSERVE/conserve2/programmation/apprentissage/python/apprendre_python3_5/exercices9/exos6")

def compare_fich(fich1 = "fich1",fich2 = "fich2") :
    f1 = open(fich1,"r")
    f2 = open(fich2,"r")
    lignes1 = f1.readlines()
    lignes2 = f2.readlines()
    i2 = 0
    if len(lignes2)>len(lignes1):
        for ligne in lignes1 :
            i = 0
            while i< len(ligne):
                if ligne[i] != lignes2[i2][i] :
                    return " {} est différent de {} ".format(ligne[i],lignes2[i2][i])
                i += 1
            i2 += 1
    else :
        for ligne in lignes2 :
            i = 0
            while i< len(ligne):
                if ligne[i] != lignes1[i2][i]:
                    return " {} est différent de {} ".format(ligne[i],lignes1[i2][i])
                i += 1
            i2 += 1
    return "Aucune difference"
    
print(compare_fich())

