
se = input('sexe ("m"ou "M" pour masculin et "f" ou "F" pour feminin): ')
nm = input('nom : ')

if se == 'M' or se == 'm':
    print("Cher Monsieur ",end = "")
    print(nm)
elif se == 'F' or se == 'f'  :
    print("Cher Mademoiselle ",end = "")
    print(nm)
else :
	print(se," n'est pas valide ")


