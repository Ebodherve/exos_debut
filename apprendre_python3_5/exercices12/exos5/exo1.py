
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
        

if __name__ == "__main__":
    cyl = Cylindre(5,7)
    print(cyl.surface())
    print(cyl.volume())
    

