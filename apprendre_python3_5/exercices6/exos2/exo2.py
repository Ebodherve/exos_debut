from math import *

def perimetre(a,b,c) :
    return a+b+c

def aire(a,b,c) :
    d = perimetre(a,b,c)/2
    return sqrt(d*(d-a)*(d-b)*(d-c))

a = float(input("entrer un coté du triangle : "))
b = float(input("entrer un deuxième coté du triangle : "))
c = float(input("entrer un troisième coté du triangle : "))
print("périmetre : ", perimetre(a,b,c))
print("aire : ", aire(a,b,c))
