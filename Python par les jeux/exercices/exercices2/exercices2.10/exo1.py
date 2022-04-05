
# Devine mon nombre

from random import randint


continuer = "oui"

nbr_essais_max = 5


# nombre choisi par l'ordinateur
# nombre proposé par le joueur
nom_joueur = input("Quel est votre nom ? ")


while continuer == "oui" :
    bsup_choix = borne_sup = 30
    trouve = 1
    binf_choix = nbr_essais = 1
    

    choice = input("choisi un nombre entre 1 et {}".format(borne_sup))
    print("Je vais le deviner en",nbr_essais_max,"tentatives au maximum !")

    while trouve != 0 and nbr_essais <= nbr_essais_max:
        print("Essai no ",nbr_essais)
        mon_nombre = randint(binf_choix,bsup_choix)

        while True :
            try :
                trouve = int(input("Votre nombre  est il : {} ?".format(mon_nombre)))
                if trouve == 0 or trouve == 1 or trouve == 2 :
                    break
                else :
                    print("entrer 0 si",mon_nombre,"est ce que vous avez choisi, 2 si il est trop petit et 1 si il est trop grand ")
            except ValueError :
                print("")
                print("entrez un nombre valide ! ")


        if trouve == 1:
            borne_sup = mon_nombre-1
        elif trouve == 2:
            binf_choix = mon_nombre + 1
        else:
            print("J'ais trouvé",mon_nombre,"en",nbr_essais,"essai(s)")
        
        nbr_essais += 1

    if nbr_essais>nbr_essais_max and trouve != 0 :
        print("J'ais utilisé mes",nbr_essais_max,"essais en vain.")
        choice = input("Quel était votre nombre :")

    continuer = input("voulez vous continuer(oui pour oui) ? ")







