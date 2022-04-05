
#recherche du nombre de caractere entre les [e,é,è,ê,ë] dans une phrase

def nb_carac_e(phrase):
    nb_e = 0
    for car in phrase:
        if car in ["e","é","è","ê","ë"]:
            nb_e += 1
    return nb_e 

print(nb_carac_e("bonjour les e,ê et é,è ainsi que ë puis, ëëë, éé,èè"))