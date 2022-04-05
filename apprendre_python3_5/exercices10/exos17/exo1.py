
#Fonction qui recopie le contenue d'un fichier dans un autre en remplacent les espaces par les trois car    caracteres -*- 
def remplace(fichier_copie,fichier_destination):
    #ouveture du fichier à copier en mode lecture
    fich_cp = open(fichier_copie,"r",encoding="Latin-1")
    #ouverture du fichier destinataire en mode ecriture
    fich_de = open(fichier_destination,"w",encoding="Utf-8")
    #extraction des lignes du fichier à copier
    lignes_copie = fich_cp.readlines()
    lignes_modifies = []
    for ligne in lignes_copie:
        ligne_courante = ""
        for char in ligne:
            if char != " ":
                ligne_courante += char
            else:
                ligne_courante += "-*-"
        lignes_modifies.append(ligne_courante)
    
    fich_de.writelines(lignes_modifies)

#execution de la fonction qui remplace les espace par des "-*-"
remplace("exercices10/exos17/fichier_copie","exercices10/exos17/fichier_destination")


