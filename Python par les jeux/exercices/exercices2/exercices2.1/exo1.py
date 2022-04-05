
print("ecrivez des mots : ")

entre = input()
nmot = 1
while(entre != "") :
    print(nmot, " : ",entre)
    entre = input('entrez un nouveau mot : ')
    nmot = nmot + 1

print("Au revoir ")
