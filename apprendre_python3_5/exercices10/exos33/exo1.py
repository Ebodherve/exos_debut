jours_semaine = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
nom_mois = ["Janvier","Fevrier","Mars","Avril","Mais","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]
numero_mois = [31,28,31,30,31,30,31,31,30,31,30,31]

def gen_jour_suiv(i):
    if i== 6:
        return 0
    else:
        return i+1

def affiche_annee():
    jour = 3
    for i in range(12):
        for j in range(numero_mois[1]):
            print(jours_semaine[jour]+" le "+str(j+1)+" "+nom_mois[i])
            jour = gen_jour_suiv(jour)

affiche_annee()
            
            
        