from random import sample

lnum = list(range(1,50))
letoile = list(range(1,11))

print("tirage au sort de cinq numeros parmis 50 et deux etoiles parmis 11 numérotées de 1 à 11 : ")
print("")

if input("entrer : 'n' pour non et n'importe quoi pour autre chose : ") != 'n' :
    nums = sample(lnum,5)
    etoile = sample(letoile,2)
    print("nombres : ",end = "")
    print(nums)
    print("étoiles : ",end = "")
    print(etoile)
