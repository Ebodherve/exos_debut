from math import pi

def donnee_sphere(fiche1,fiche2):
    f1 = open(fiche1,mode ="r")
    f2 = open(fiche2,mode="w")
    for nbr in f1.readlines():
        dim = float(nbr)
        f2.write("Diam. {:0.2f} section {:0.2f} Surf. {:0.2f} Vol. {:0.2f} \n".format(dim,dim**2*pi/4,dim**2*pi,dim**3*pi/6))

fich1 = "exercices10/exos25/"+input("fichier contenant les diametres :")
fich2 = "exercices10/exos25/"+input("fichier contenant les dimensions:")

donnee_sphere(fich1,fich2)
