
class Satellite(object):
    def __init__(self, nom, masse = 100, vitesse = 0):
        self.nom = nom
        self.masse = masse
        self.vitesse = vitesse
    def impulsion(self,force,duree):
        self.vitesse += (force*duree/self.masse)
    def affiche_vitesse(self):
        print("Le satellite {} a une vitesse de : {}m/s ".format(self.nom,self.vitesse))
    def energie(self) :
        return (self.masse*self.vitesse**2)/2
    
sat1 = Satellite('zoé',masse=250,vitesse= 10)
sat1.impulsion(500,15)
sat1.affiche_vitesse()
print(sat1.energie())

sat1.impulsion(500,15)
sat1.affiche_vitesse()
print(sat1.energie())
         
    
    



