
import math

class Cercle(object) :
    def __init__(self,r):
        self.rayon = r
    def surface(self):
        return self.rayon**2*math.pi
    

class Cylindre(Cercle) :
    def __init__(self,r,h):
        Cercle.__init__(self,r)
        self.hauteur = h
    def volume(self):
        return self.surface()*self.hauteur
        

class Cone(Cylindre):
    def __init__(self,r,h):
        Cylindre.__init__(self,r,h)
    def volume(self):
        return Cylindre.volume(self)/3
    


if __name__ == "__main__":
    co = Cone(5,7)
    print(co.surface())
    print(co.volume())
    

