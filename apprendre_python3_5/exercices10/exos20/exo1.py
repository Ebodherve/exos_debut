from os import system


#script permettant d'explorer les caracteres entre un min et un max 
"""
def affiche():
    min = int(input("min des caracteres : "))
    max = int(input("max des caracteres : "))
    for i in range(min,max):
        try :
            print("code en nombre de {} ---> ".format(i),chr(i))
        except UnicodeEncodeError:
            print("impossible d'afficher une caracter de avec pour identifiant :",i)
            break

continuer = True
while continuer:
    affiche()
    entrer = input("appuyer en pour recomancer et ecrivez autre chose pour pour ne plus continuer")
    system("clear")
    if entrer != "":
        continuer = False

"""

#script permettant d'afficher les caracteres de l'alphabet cyrillique
def cyrillique():
    for i in range(1040,1328):
        print(chr(i))

cyrillique()
