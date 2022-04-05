from pprint import pprint

def lcar_occ(texte) :
    histo = {}
    for car in texte :
        if car in histo :
            histo[car] += '|'
        else :
            histo[car] = '|'
    return histo

t = "bonjour ! Vous etes sur notre site de ventes de vetements"
print(t)
pprint(lcar_occ(t))
