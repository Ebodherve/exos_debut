

def poly3(x) :
    return 2*(x**3) - (3*x) - 1

def tabuler(binf, bsup, pas) :
    evolution = binf

    while evolution <= bsup :
        print(evolution,"   ",poly3(evolution))
        evolution += pas

binf = float(input("borne inferieur : "))
pas = float(input("pas : "))
bsup = float(input("borne superieur : "))

tabuler(binf,bsup,pas)


