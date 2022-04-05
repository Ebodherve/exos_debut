
a = int(input("premier nombre : "))
b = int(input("deuxieme nombre : "))

if a>b : 
    c = a
    a = b
    b = c
cpt = a+1

s = []
s2 = 0

while cpt != b : 
    if (cpt%3 == 0) or (cpt%5 == 0) :
        s.append(cpt)
    cpt = cpt + 1

print('somme des multiples de 3 et 5 entre :',a, "et",b )

if len(s) > 0 :
	i = 0
	while i <= len(s)-1 :
	    s2 = s2 + s[i]
	    print(s[i],'+', end = "")
	    i = i+1
	print('=',s2)
else :
	print("Il n'y a pas de multiple commun à 3 ou 5 entre ",a," et ",b)


