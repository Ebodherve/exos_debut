
def arrondi_decimal(nombre):
    puis_dix = len(nombre.split(".")[1])-1
    if nombre[-2] == '5':
        return str(float(nombre)*10**(puis_dix-1))+"e-"+str(puis_dix-1)
    else:
        return str(float(nombre)*10**(puis_dix))+"e-"+str(puis_dix)

def traite_fich(fich1,fich2):
    f1 = open(fich1, mode = 'r')
    f2 = open(fich2, mode = 'w')
    for nb_f in f1.readlines():
        f2.write(arrondi_decimal(nb_f)+"\n")
    f1.close()
    f2.close()


fich1 = "exercices10/exos26/"+input("fichier contenant les floattant :")
fich2 = "exercices10/exos26/"+input("fichier contenant les floattants convertis:")

traite_fich(fich1,fich2)