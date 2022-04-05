
class JeuDeCartes(object) :
    def __init__(self):
        self.liste_cartes = []
        for i in range(2,15,1):
            for j in range(4):
                self.liste_cartes.append((i,j))
        self.liste_corresp_carte = {0:"Coeur",1:"Carreau",2:"Trèfle",3:"Pique",4:"rouge",5:"bleu",6:"vert",
                                 7:"gris",8:"jaune",9:"orange",10:"noire",11:"valet",12:"dame",13:"roi",14:"as"}
    def nom_carte(self,dval):
        if dval[0] in [i for i in range(2,15,1)] and dval[1] in [i for i in range(4)]:
            return " {} de {} ".format(self.liste_corresp_carte[dval[0]],self.liste_corresp_carte[dval[1]])
        else :
            return "carte non existante !"
    def battre(self) :
        shuffle(self.liste_cartes)
    def tirer(self):
        if len(self.liste_cartes) == 0:
            return None
        else :
            result_tir = self.liste_cartes[0]
            self.liste_cartes.remove(self.liste_cartes[0])
            return result_tir

if __name__ == "__main__" :
    from random import shuffle,choice

    jeu = JeuDeCartes()
    jeu.battre()
    for n in range(53):
        c = jeu.tirer()
        if c == None:
            print('Terminé !')
        else:
            print(jeu.nom_carte(c))



