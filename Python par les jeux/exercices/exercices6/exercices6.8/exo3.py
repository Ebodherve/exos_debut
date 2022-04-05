from random import randint

#jeux des echelles
#minimisation du nombre de lancés

#differentes parties du jeux 

#lancer du joueur et deplacement
def lance_deplace():
    #lancer du dée
    deplacement = randint(1,6)+joueur['coord']
    #verification du résultats 
    for i,j in cases_j_echelle.items() :
        #si le resultat est un serpent ou une echelle
        if i[0] == deplacement :
            #alors renvoit à la queu du serpent ou en haut de l'echelle
            if j == 'echelle' or j == 'serpent':
                deplacement =  i[1]
                joueur['liste_deplace_s_e'].append(i[1]-i[0])
                break
    #si resultat > 100 faire reculer le joueur de la valeur supplémentaire  
    if  deplacement > 100 :
        deplacement -= (deplacement % 100)*2
            
    joueur['coord'] = deplacement 
    joueur['nbr_coups'] += 1

#jeu
def jeu() :
    while joueur['coord'] != 100 :
        lance_deplace()

#initialisation des informations sur le joueur
def init_joueur():
    joueur['nbr_coups'] = 0     
    joueur['liste_deplace_s_e'] = []
    joueur['coord'] = 1

#affichage d'une partie de jeux
def affiche_partie():
    print("nombre de coups : {}".format(joueur['nbr_coups']))
    print("liste des deplacements : {}".format(joueur['liste_deplace_s_e']))
    print("coordonnée du joueur : {}".format(joueur['coord']))

#procedure de simulation de nbr partie
def simule_parties(nbr):
    global somme_coups
    somme_coups = 0
    for i in range(nbr) :
        print("partie  {} :".format(i+1))
        jeu()
        somme_coups += joueur['nbr_coups']
        affiche_partie()
        init_joueur()
        print("")

#verification de la bonne disposition des 
# echelles et serpents sur les cases  
def verif_dispo() :
    liste_coordonees = [i for i in cases_j_echelle.keys()]
    posi = 1
    for i in  liste_coordonees[:-1]:
        for j in liste_coordonees[posi:] :
            if i[0] in j or i[1] in j :
                return False,i,j
        posi += 1
    return True,""


#liste des echelles 'e' et serpents 's'

#echelles 
cases_j_echelle = {(80,100):'echelle'}
cases_j_echelle[(71,91)] ='echelle'
cases_j_echelle[(51,67)] ='echelle'
cases_j_echelle[(28,84)] ='echelle'
cases_j_echelle[(21,42)] ='echelle'
cases_j_echelle[(1,38)]  ='echelle'
cases_j_echelle[(4,14)]  ='echelle'
cases_j_echelle[(9,31)]  ='echelle'

#serpents (déplacement horizontale des serpents 
# pour la minimisation des déplacements)
cases_j_echelle[(77,79)] ='serpent'
cases_j_echelle[(75,72)] ='serpent'
cases_j_echelle[(70,68)] ='serpent'
cases_j_echelle[(64,60)] ='serpent'
cases_j_echelle[(30,24)] ='serpent'
cases_j_echelle[(27,22)] ='serpent'
cases_j_echelle[(36,34)] ='serpent'
cases_j_echelle[(11,7)] ='serpent'


#somme des coups de (n) parties
global somme_coups

#données du joueur
#nombre de coups : nbr_coups et liste des deplacement sur echelle ou serpent liste_deplace_s_e 
# coordonnée du joueur : coord
joueur = {'nbr_coups':0, 'liste_deplace_s_e' : [], 'coord' : 1}
        
#simulation de n parties
"""n = 10000 
simule_parties(n)
print("nombre moyen de lancés des : {} ".format(somme_coups/n))
"""


bien_placer = verif_dispo()
if bien_placer[0] :
    n = 10000 
    simule_parties(n)
    print("nombre moyen de lancés des : {} ".format(somme_coups/n))
else :
    print(bien_placer[1],bien_placer[2])

