
def tri_liste(liste):
    taille = len(liste)
    for i in range(1,taille):
        j = i
        cle = liste[i]
        while j > 0 and cle<liste[j-1]:
            liste[j] = liste[j-1]
            j -= 1
        liste[j] = cle

#liste = ["z","o","g","k","a","m","p","l","b","p"]
liste = [4,3,1,5,4,9,50,48]
print(liste)
tri_liste(liste)
print(liste)
