from exo1_18 import voyelles

#fonction qui compte le nombre de caractere dans une phrase
def compteVoyelles(phrase):
    nbr = 0
    for car in phrase:
        if voyelles(car):
            nbr += 1
    return nbr

phrase = "cette phrase contient des caraceteres d'un certain nombre type en particulier des voyelles"

print("le nombre de voyelle de la phrase :",phrase," est :",compteVoyelles(phrase))
