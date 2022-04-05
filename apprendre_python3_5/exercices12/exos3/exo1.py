
class Voiture(object):
    def __init__(self,marque = 'Ford',couleur = 'red'):
        self.marque = marque
        self.couleur = couleur
        self.pilote = 'personne'
        self.vitesse = 0
    def choix_conducteur(self,nom):
        self.pilote = nom
    def accelerer(self,taux,duree):
        if self.pilote != 'personne':
            self.vitesse += taux*duree
        else :
            print("Cette voiture n'a pas de conduction ")
    def affiche_tout(self):
        print("{} est pilotée par {} à une vitesse de : {}m/s ".format(self.marque,self.pilote,self.vitesse))
    
vt1 = Voiture('Peugeot','blue')
vt2 = Voiture(couleur='green')
vt3 = Voiture('Mercedes')

vt1.choix_conducteur('Roméo')
vt2.choix_conducteur('anaîs')
vt2.accelerer(1.8,12)
vt3.accelerer(1.9,11)
vt2.affiche_tout()
vt3.affiche_tout()


