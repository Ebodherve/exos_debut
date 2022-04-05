
def le_plus_long(phrase):
    l_mots = phrase.split()
    mot_long = ""
    for mot in l_mots:
        if len(mot)> len(mot_long):
            mot_long = mot
    return mot_long
print("entrez votre phrase : ")
print("le plus long de votre phrase est : ",le_plus_long(input()))