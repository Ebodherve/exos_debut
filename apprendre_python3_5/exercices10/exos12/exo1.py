
def estUneMaj(param):
    return "A"<=param<="Z" or param in ["É","Ê","Ë","È","Ÿ","Ô","Û","Î","Ṏ","Ï","Ä"]


def chaineListe(chaine):
    begwords = [0]
    endwords = []
    indword = 0
    taille = len(chaine)
    liste = []
    while indword < taille :
        if chaine[indword] != " ":
            if indword == taille-1:
                endwords.append(indword+1)
            elif chaine[indword+1] == " ":
                endwords.append(indword+1)
            if indword >0:
                if chaine[indword-1] == " ":
                    begwords.append(indword)
        indword += 1
    indword = 0
    while indword < len(begwords)-1:
        liste.append(chaine[(begwords[indword]):(endwords[indword])])
        indword += 1
    return liste

def maj_pword(phrase):
    liste_mot = chaineListe(phrase)
    liste_mot_Maj = []
    for mot in liste_mot:
        if estUneMaj(mot):
            liste_mot_Maj.append(mot)
    return liste_mot_Maj


print(maj_pword("Liste des mots En majuscule De Notre text"))