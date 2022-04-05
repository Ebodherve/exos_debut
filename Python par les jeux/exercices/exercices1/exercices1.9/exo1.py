from random import randint, choice

tetra = [1,2,3,4]
hexa = 6
octa = 8
deca = 10
icosa = 12

print("lancé du tétraedre, face : ", end = "")
lance = choice(tetra)
print(lance)

if lance == 1:
    print("1 - correspond à un cube : ")
    print("le lancer du cube donne : ",randint(1,hexa))
elif lance == 2:
    print("2 - correspond à un octaèdre : ")
    print("le lancer d'un octaèdre donne : ", randint(1,octa))
elif lance == 3 :
    print("3 - correspond à un dodécaedre : ")
    print("le lancer d'un dodécaedre donne : ",randint(1,deca))
else :
    print("4 - correspond à un icosaèdre")
    print("le lancer d'un isocaèdre donne : ",randint(1,icosa))





