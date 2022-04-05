
def tri_nom(fich1,fich2):
    f1 = open(fich1,mode="r")
    f2 = open(fich2,mode= "w")
    lignes = f1.readlines()
    lignes.sort()
    f2.writelines(lignes)
    f1.close()
    f2.close()

fich1 = "exercices10/exos34/"+input("fichier contenant les noms :")
fich2 = "exercices10/exos34/"+input("fichier contenant les noms trié:")

tri_nom(fich1,fich2)


#print(open("exercices10/exos34/fich1",mode="r").readlines())