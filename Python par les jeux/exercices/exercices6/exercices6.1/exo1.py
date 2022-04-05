from pprint import pprint

"""char_mois = "janvier","février","mars","avril","mais","juin","julliet","aout","septembre","octobre","novembre","Décembre"
nombre_mois = 31,28,31,30,31,30,31,31,30,31,30,31
mois_annees = {}"""

mois_annees = {"janvier":31,"février":28,"mars":31,"avril":30,"mais":31,"juin":30,"julliet":31,"aout":31,"septembre":30,"octobre":31,"novembre":30,"Décembre":31}

"""j = 0

for i in char_mois :
    mois_annees[char_mois] = nombre_mois[j] 
    j += 1"""
    

#print(mois_annees.items())
pprint(mois_annees)
