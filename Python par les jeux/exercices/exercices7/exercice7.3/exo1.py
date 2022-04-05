
ensvo = ['e','o','a','u','y','i','é','à','è']
mot = input("entrer un mot : ")

for i in range(len(mot)) :
    if mot[i] in ensvo :
        mot = mot[:i]+"*"+mot[i+1:]
    
print(mot)
