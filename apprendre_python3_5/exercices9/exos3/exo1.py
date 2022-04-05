from os import chdir

chdir("/home/tsanga/Bureau/CONSERVE/conserve2/programmation/apprentissage/python/apprendre_python3_5/exercices9/exos3")

def multdn(n1,n2) :
    return str(n1)+'x'+str(n2)+" = {} ".format(n1*n2)

def generefich_table(nom) :
    fiche = open(nom,"w")
    for i in range(2,30):
        for j in range(1,20) :
            fiche.write(multdn(i,j)+"\n")
    fiche.close()
    
    
generefich_table("table_mult.txt")    
    

