
def nbmot_phrase(phrase):
    indcar = 0
    nbmot = 0
    taille = len(phrase)
    while indcar<taille :
        if phrase[indcar]!=" ":
            if indcar==taille-1 : 
                nbmot += 1
            elif phrase[indcar+1]==" ":
                nbmot += 1
        indcar += 1
    return nbmot


print(nbmot_phrase("   bonjour à tous nous allons compoter le nombre de mot de cette phrase "))
        
