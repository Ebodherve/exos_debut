from os import chdir
from exo1 import *

chdir("/home/tsanga/Bureau/CONSERVE/conserve2/programmation/apprentissage/python/apprendre_python3_5/exercices9/exos12")


file = open("fich_var","a")

a = 1
b = "str"
conserve_vtype(file,a)
conserve_vtype(file,b)

file.close()
file = open("fich_var","r")

c = var_type(file)
d = var_type(file)


print(c,d)

#print(len(file.readline()))
#print(len(file.readline()))
