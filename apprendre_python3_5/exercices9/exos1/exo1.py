
nf  = input('entrez le nom du fichier :')
file = open(nf,"a")
choix = input("ajouter(aj)/afficher(af)) le contenu du fichie : ")
continuer = False
if choix == "aj":
    continuer = True
elif choix == "af" :
    file.close()
    file = open(nf,"r")
    print(file.read())
    file.close()
else :
    pass    

while continuer :
    ligne = input()
    if ligne == "":
        continuer = False
    ligne += "\n"
    file.write(ligne)
    
file.close()
