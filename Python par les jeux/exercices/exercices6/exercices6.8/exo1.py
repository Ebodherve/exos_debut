from random import randint

#jeux des echelles

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

#serpents
cases_j_echelle[(98,79)] ='serpent'
cases_j_echelle[(95,75)] ='serpent'
cases_j_echelle[(93,73)] ='serpent'
cases_j_echelle[(64,60)] ='serpent'
cases_j_echelle[(87,24)] ='serpent'
cases_j_echelle[(62,19)] ='serpent'
cases_j_echelle[(54,34)] ='serpent'
cases_j_echelle[(17,7)] ='serpent'

#somme des coups de (n) parties
global somme_coups

#données du joueur
#nombre de coups : nbr_coups et liste des deplacement sur echelle ou serpent liste_deplace_s_e 
# coordonnée du joueur : coord
joueur = {'nbr_coups':0, 'liste_deplace_s_e' : [], 'coord' : 1}
        
#simulation de n parties
n = 10000 
simule_parties(n)
print("nombre moyen de lancés des : {} ".format(somme_coups/n))
