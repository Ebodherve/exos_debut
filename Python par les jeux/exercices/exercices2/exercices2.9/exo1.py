
# Devine mon nombre
from random import randint

nbr_essais_max = 5

borne_sup = 30
mon_nombre = randint(1,borne_sup)
ton_nombre = 0
nbr_essais = 1

# nombre choisi par l'ordinateur
# nombre proposé par le joueur
nom_joueur = input("Quel est votre nom ? ")
print("J'ai choisi un nombre entre 1 et",borne_sup)
print("A vous de le deviner en",nbr_essais_max,"tentatives au maximum !")

while ton_nombre != mon_nombre and nbr_essais <= nbr_essais_max:
    print("Essai no ",nbr_essais)
    ton_nombre = int(input("Votre proposition : "))
    if ton_nombre < mon_nombre:
        print("Trop petit")
    elif ton_nombre > mon_nombre:
        print("Trop grand")
    else:
        print("Bravo, ",nom_joueur,"! Vous avez trouvé",mon_nombre,"en",nbr_essais,"essai(s)")
    nbr_essais += 1

if nbr_essais>nbr_essais_max and ton_nombre != mon_nombre :
    print("Désolé, vous avez utilisé vos",nbr_essais_max,"essais en vain.")
    print("J'avais choisi le nombre",mon_nombre,".")


