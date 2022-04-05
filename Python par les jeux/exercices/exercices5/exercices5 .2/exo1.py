
liste1 = [31,28,31,30,31,30,31,31,30,31,30,31]

liste2 = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']

j = -1
for i in range(12) :
    j += 2
    liste2[j:j] = [liste1[i]]

liste2[4:4] = [29]

print(liste2)

