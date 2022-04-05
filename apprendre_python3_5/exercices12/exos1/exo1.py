

class Domino(object):
    def __init__(self,a = 0,b = 0):
        self.a = a
        self.b = b
    def affiche_point(self):
        print("face A : {}, face B : {} ".format(self.a,self.b))
    def valeur(self):
        return self.a + self.b

d1 = Domino(4,8)
d2 = Domino(9,7)
d1.affiche_point()
d2.affiche_point()

print("Total des points : {} ".format(d1.valeur() + d2.valeur()))

liste_dominos = []

for i in range(7) : 
    liste_dominos.append(Domino(6,i+1))
    
print(liste_dominos[3])
