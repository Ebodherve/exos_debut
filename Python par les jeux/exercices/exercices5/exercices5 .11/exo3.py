
jour_semaine = ("dimanche","lundi","mardi","mercredi","jeudi","vendredi","samedi") 

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
     


print("Liste des vendredis 13 de la semaine : ")

#recherche des 13 qui sont des vendredis

for i in range(2000,2099,1) :
    for j in range(1,12,1) :
        if "vendredi" == jour_semaine[jour_sem(13,j,i)] :
            print("vendredi/{}/{}/{}".format(13,j,i))




