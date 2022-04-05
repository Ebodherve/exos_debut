table = []
for i in [2,3,5,7,11,13,17,19]:
    ligne = []
    for j in range(1,8):
        ligne.append(i*j)
    table.append(ligne) 
for i in table:
    for j in i:
        print(j,"",end="")
    print("")