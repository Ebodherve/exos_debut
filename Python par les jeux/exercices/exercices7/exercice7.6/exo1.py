

def traduit_mot(mot) :
    i = 0
    if mot[0] in voyelles:
        mot = "av" + mot
        i = 2

    while i < len(mot)-1 :
        if mot[i] not in voyelles :
            if mot[i+1] in voyelles :
                mot = mot[:i+1] + "av" + mot[i+1:]
                i+=3
            else :
                i+=1
        else :
            i += 1
    return mot

def traduit_phrase(phrase) :
    nv_liste = phrase.split()
    phrase_ret = ""
    for mot in nv_liste :
        phrase_ret += traduit_mot(mot)+" "
    return phrase_ret

voyelles = ['e','a','u','i','o','y','é','è']
phrase = input("entrez une phrase : ")

print("Traduction en javanais : ")
print(traduit_phrase(phrase))
