from math import pi, sqrt


def periode(lg) :
    return (2*pi*sqrt(l/9.87))

l = float(input("entrer la longueur du pendule : "))
print("sa periode est de : ", periode(l), end = "")
print("s")


