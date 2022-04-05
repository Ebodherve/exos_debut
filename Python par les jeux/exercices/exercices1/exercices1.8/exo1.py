from random import random

pacr = []

for i in range(5) :
    rnd = random()
    if rnd < 0.01:
        pacr.append("L")
    elif rnd < 0.04:
        pacr.append("E")
    elif rnd < 0.23 :
        pacr.append("R")
    else :
        pacr.append("C")


est_pac = False

carte1 = pacr[0]

for carte in pacr :
    if carte1 != carte :
        est_pac = True
    carte1 = carte

if est_pac:
    print("pacquet de cinq cartes : ", pacr)
else:
    print("pacquet de cinq cartes : ", pacr)
    print("pacquet de cartes non valide : ")

        



