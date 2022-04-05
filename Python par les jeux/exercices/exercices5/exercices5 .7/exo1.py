from random import choice,randint

def lance_de() :
    return choice(f_dee)

#action ation apres lancée
def lance_action(result) :
    global n_p_puzzle
    if result == c_poirier[0] :
        if c_poirier[1] == 0 :
            return 0
        else :
            c_poirier[1] -= 1
            return 1
    elif result == c_pommier[0] :
        if c_pommier[1] == 0 :
            return 0
        else :
            c_pommier[1] -= 1
            return 1
    elif result == c_cerisier[0] :
        if c_cerisier[1] == 0 :
            return 0
        else :
            c_cerisier[1] -= 1
            return 1
    elif result == c_prunier[0] :
        if c_prunier[1] == 0 :
            return 0
        else :
            c_prunier[1] -= 1
            return 1
    elif result == "corbeau" :
        n_p_puzzle += 1
        return 0
    else :
        return 2

def arbres_vide() :
    if c_poirier[1] != 0 :
        return False
    elif c_pommier[1] != 0 :
        return False
    elif c_prunier[1] != 0 :
        return False
    elif c_cerisier[1] != 0 :
        return False
    else :
        return True

def partie() :
    global p_j1,p_j2,p_j3,p_j4
    global gagne,nb_coup_partie
    nb_coup_partie = 0
    while n_p_puzzle != 9 and not arbres_vide() : 
        #joueur 1
        resultat = lance_action(lance_de())
        if(resultat == 2) :
            r1 = lance_action(choice(f_dee[:4]))
            r2 = lance_action(choice(f_dee[:4]))
            p_j1 += r1+r2
        else :
            p_j1 += resultat
        #joueur 2
        resultat = lance_action(lance_de())
        if(resultat == 2) :
            r1 = lance_action(choice(f_dee[:4]))
            r2 = lance_action(choice(f_dee[:4]))
            p_j2 += r1+r2
        else :
            p_j2 += resultat
        #joueur 3
        resultat = lance_action(lance_de())
        if(resultat == 2) :
            r1 = lance_action(choice(f_dee[:4]))
            r2 = lance_action(choice(f_dee[:4]))
            p_j3 += r1+r2
        else :
            p_j3 += resultat
        #joueur 4
        resultat = lance_action(lance_de())
        if(resultat == 2) :
            r1 = lance_action(choice(f_dee[:4]))
            r2 = lance_action(choice(f_dee[:4]))
            p_j4 += r1+r2
        else :
            p_j4 += resultat
        nb_coup_partie += 4
    if(n_p_puzzle == 9) :
        gagne = False
    else :
        gagne = True
                
def init() :
    global n_p_puzzle
    global p_j1,p_j2,p_j3,p_j4,n_p_puzzle
    
    p_j1,p_j2,p_j3,p_j4,n_p_puzzle = 0,0,0,0,0
    n_p_puzzle = 0
    c_prunier[1],c_pommier[1],c_poirier[1],c_cerisier[1] = 10,10,10,10

    

def simule_parties(nb_p) :
    global nb_coup_partie
    #nombre de partie gangner et nombre total de coups
    nbp_gagner,nb_t_coups = 0,0
    for i in range(nb_p) :    
        partie()
        nb_t_coups += nb_coup_partie
        if(gagne) :
            nbp_gagner += 1
        init()
    return nbp_gagner,nb_t_coups/nb_p



#arbres
c_prunier = ["blue",10]
c_pommier = ["green",10]
c_poirier = ["yellow",10]
c_cerisier = ["red",10]

#puzzle_corbeau

#dé
f_dee = ["blue","green","yellow","red","corbeau","panier"]

#panier

global p_j1,p_j2,p_j3,p_j4,n_p_puzzle

p_j1,p_j2,p_j3,p_j4,n_p_puzzle = 0,0,0,0,0

global gagne,nb_coup_partie

nb_coup_partie = 0
gagne = False

nb_vic,nb_m_coup_partie = simule_parties(100000)
print("nombre de vitoires {}, nombre moyen de coups par partie {}".format(nb_vic,nb_m_coup_partie))


