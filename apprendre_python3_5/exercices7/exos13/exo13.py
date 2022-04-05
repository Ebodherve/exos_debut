
def compteMots(ph) :
    nbmots = 0
    for i in ph :
        if i == " ":
            nbmots += 1
    if i != " ":
        nbmots += 1
    return nbmots




print(compteMots("bonjour aux fonctions en python "))

