
jour_semaine = ("dimanche","lundi","mardi","mercredi","jeudi","vendedi","samedi") 

def jour_sem(nj,m,an) :
    if m<3 :
        z = an-1
    else :
        z = an
    
    k = ((23*m)//9) + nj + 4 + an + z//4 - z//100 + z//400
    
    if m<3 :
        j = k%7
    else :
        j = (k-2)%7
    return j  
     
nj = int(input("numero du jour : "))
m = int(input("numero du mois : "))
an = int(input("numero de l'année : "))

print("jour de la semaine : ",jour_semaine[jour_sem(nj,m,an)])


