
#chaine = "12ê45"

#print(chaine[4]+chaine[3]+chaine[2]+chaine[1]+chaine[0])


def inverse_5(chaine):
    taille = len(chaine)
    tunite = taille//5
    debut = taille - tunite
    fin = taille
    
    for i in range(4):
        print(chaine[debut:fin],end = "")
        fin -= tunite
        debut = fin-tunite
    print(chaine[:fin])

#inversion des 5 fragments d'une chaine 

chaine = "qui sont ces serpents qui siffles sur nos tete"
print(chaine)
inverse_5(chaine)
chaine = "bonjour à vous et nous"
print(chaine)
inverse_5(chaine)    

 




