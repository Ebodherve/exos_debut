
# fonction qui compte le nombre mots contenut dans le texte un 
# fichier texte dont le nom est passé en parametre
def nbr_mots(nom_fich):
    fichier = open(nom_fich,mode='r')
    nbr = 0
    for ligne in  fichier.readlines():
        nbr += len(ligne.split())
    return nbr

nom = "exercices10/exos23/"+input("entrez le nom du fichier dont on doit le nombre caractere : ")
print("ce fichier comporte {} mots".format(nbr_mots(nom)))
