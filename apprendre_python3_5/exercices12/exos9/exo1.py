
class CompteBanquaire(object) :
    
    def __init__(self,nom = 'Dupont',solde = 1000):
        self.nom = nom
        self.solde = solde
    def depot(self,somme):
        self.solde += somme
    def retrait(self,somme):
        self.solde -= somme
    def affiche(self):
        print("Le solde du compte banquaire de {} est : {} francs".format(self.nom,self.solde)) 
        

class CompteEpargne(CompteBanquaire):
    def __init__(self,nom = "Dupont",solde = 1000,taux = 0.003) :
        CompteBanquaire.__init__(self,nom,solde)
        self.taux = taux
    def changetaux(self,valeur) :
        self.taux = valeur
    def capitalisation(self,nbmois) :
        print("capitalisation sur {} mois avec un taux mensuel de {} ".format(int(nbmois),self.taux))
        for i in range(int(nbmois)):
            self.solde += self.solde*self.taux


c1 = CompteEpargne("Duval",600)
c1.depot(350)
c1.affiche()
c1.capitalisation(12)
c1.affiche()
c1.changetaux(0.5)
c1.capitalisation(12)
c1.affiche()


"""
compte1 = CompteBanquaire('Duchmol',800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()

compte2 = CompteBanquaire()
compte2.depot(25)
compte2.affiche()
"""

