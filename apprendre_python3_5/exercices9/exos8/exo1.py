from os import chdir

chdir("/home/tsanga/Bureau/CONSERVE/conserve2/programmation/apprentissage/python/apprendre_python3_5/exercices9/exos8")

def ajout_info_mem(nf = "club") :
    fic = open(nf,"a")
    print("entrer votre nom,prenom,adresse,code postale et numero de telephone : ")
    nom = input("nom : ")
    prenom = input("prenom : ")
    ad = input("adresse : ")
    codep = input("code postale : ")
    ntel = input("numero de telephone : ")
    
    fic.write(nom+"\n")
    fic.write(prenom+"\n")
    fic.write(ad+"\n")
    fic.write(codep+"\n")
    fic.write(ntel+"\n")
    fic.write("\n")
    fic.close()

while input("ajouter un membre dans le club ('o' pour oui) : ") == "o":
    ajout_info_mem()

