
def fusionne(fich1,fich2):
    f1 = open(fich1,mode ="r")
    f2 = open(fich2,mode = 'w')
    lignes1 =f1.readlines()
    ligne_precedente = 0
    for ligne in lignes1[1:]:
        if ligne[0]<"A" or ligne[0]>"Z":
            lignes1[ligne_precedente] = lignes1[ligne_precedente][:-1]
        ligne_precedente += 1
    f2.writelines(lignes1)
    f1.close()
    f2.close()

nf1 = "exercices10/exos24/" + input()
nf2 = "exercices10/exos24/" + input()

fusionne(nf1,nf2)
