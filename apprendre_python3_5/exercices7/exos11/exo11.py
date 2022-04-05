
mois_ann = ["janvier","février","mars","avril","mais","juin","juillet","août","septembre","octobre","novembre","decembre"]

def nomMois(num):
    if 0<num and num<13 :
        return mois_ann[num-1]
    else :
        return "numero de mois inexistant"


print(nomMois(-1))
