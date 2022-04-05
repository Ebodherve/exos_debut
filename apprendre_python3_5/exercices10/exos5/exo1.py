
def compteCar(chaine,car):
    nbcar = 0
    for c in chaine :
        if c==car :
            nbcar += 1
    return nbcar

print(compteCar("ananas au jus","a"))
print(compteCar("Gédéon est déjà là","é"))
