# dilemme du prisonnier itéré, version duel
from random import choice
choix = ['T','C']

# T : trahit, C : coopère

def gain(lui,moi):
    if lui=='C' and moi=='C':
        return 3
    elif lui=='C' and moi=='T':
        return 5
    elif lui=='T' and moi=='C':
        return 0
    elif lui=='T' and moi=='T':
        return 1


# Le tournoi
liste = {}
strategie = {}
score = {}

duel = {}
# ajouter des joueurs ci-dessous, selon les modèles des joueurs existants
# commencer ici
liste['Toujours seul'] = []
liste['Bonne poire'] = []
liste['Majorité'] = []
liste['Aléatoire'] = []
liste['Donnant donnant'] = []
liste['autre_donnant'] = []
liste['gagne_majorite'] = []
liste['troisieme_donnant'] = []

# Toujours seul
# ne coopère jamais
def toujours_seul(liste_lui,liste_moi):
    return 'T'
# Bonne poire
# coopère toujours
def bonne_poire(liste_lui,liste_moi):
    return 'C'

# Aléatoire
# joue avec une probabilité égale 'T' ou 'C'
def aleatoire(liste_lui,liste_moi):
    global choix
    return choice(choix)

# Donnant donnant
# coopère seulement si l'autre joueur a coopéré au coup précédent.
def donnant_donnant(liste_lui,liste_moi):
    if len(liste_lui)>0:
        return liste_lui[-1]
    else: # premier coup
        return 'C'
# Majorité
# coopère seulement si l'autre joueur a coopéré en majorité.
def majorite(liste_lui,liste_moi):
    if len(liste_lui)>0:
        if liste_lui.count('C') > len(liste_lui)//2:
            return 'C'
        else:
            return 'T'
    else: # premier coup
        return 'C'

#autres stratégies

#ne joue la strategie donnant_donnant que si l'autre joueur fait 
# pareille et joue et dans le cas contraire joue son premier choix
def autre_donnant(liste_lui,liste_moi) :
    if len(liste_lui) == 0 :
        return 'C'
    elif liste_lui == liste_moi or liste_lui[:-1] == liste_moi or liste_moi[:-1] == liste_lui:
        return liste_lui[-1]
    else :
        return liste_lui[0]

# contre la strategie majoritaire à tout les  coups
def gagne_majorite(liste_lui,liste_moi) :
    if len(liste_moi) <= 2:
        return 'C'
    elif liste_moi[-1] == 'C' :
        return 'T'
    else :
        return 'C'

#ne joue la strategie donnant_donnant que si l'autre joueur fait 
# pareille et joue et dans le cas contraire joue la strategie majoritaire
def troisieme_donnant(liste_lui,liste_moi) :
    if len(liste_lui) == 0 :
        return 'C'
    elif liste_lui == liste_moi or liste_lui[:-1] == liste_moi or liste_moi[:-1] == liste_lui:
        return liste_lui[-1]
    else :
        return majorite(liste_lui,liste_moi)


# ...
strategie['Toujours seul'] = lambda lui, moi : toujours_seul(lui,moi)
strategie['Bonne poire'] = lambda lui, moi : bonne_poire(lui,moi)
strategie['Majorité'] = lambda lui, moi : majorite(lui,moi)
strategie['Aléatoire'] = lambda lui, moi : aleatoire(lui,moi)
strategie['Donnant donnant'] = lambda lui, moi : donnant_donnant(lui,moi)
strategie['autre_donnant'] = lambda lui,moi : autre_donnant(lui,moi)
strategie['gagne_majorite'] = lambda lui,moi : gagne_majorite(lui,moi)
strategie['troisieme_donnant'] = lambda lui,moi : troisieme_donnant(lui,moi)

# ...
# terminer là
nb_total_coups = 10  # à modifier

for joueur in liste.keys():
    score[joueur] = 0


for i in liste.keys(): # i et j sont les joueurs
    for j in liste.keys() :
        liste[i] = []        # on recommence une partie
        liste[j] = []
        if i>=j:
            nb_coups = 0
            score_joueur1 = 0
            score_joueur2 = 0
            while nb_coups < nb_total_coups :
                coup_joueur1 = strategie[i](liste[j],liste[i])
                coup_joueur2 = strategie[j](liste[i],liste[j])
                liste[i].append(coup_joueur1)
                if i!=j:
                    liste[j].append(coup_joueur2)
                score_joueur1 += gain(coup_joueur2,coup_joueur1)
                score_joueur2 += gain(coup_joueur1,coup_joueur2)
                nb_coups += 1
            duel[(i,j)] = score_joueur1
            if i!=j:
                duel[(j,i)] = score_joueur2
            score[i] += score_joueur1
            if i!=j:
                score[j] += score_joueur2
# affichage des résultats

def trie_par_valeur(d):
    #retourne une liste de tuples triée selon les valeurs
    return sorted(d.items(), key=lambda x: x[1])

def trie_par_cle(d):
    #retourne une liste de tuples triée selon les clés
    return sorted(d.items(), key=lambda x: x[0])
score_trie = trie_par_valeur(score)
score_trie.reverse()

for i in range(0,len(score_trie)):
    print(score_trie[i][0],":",score_trie[i][1])
print()
duel_trie = trie_par_cle(duel)

for i in range(0,len(duel_trie)):
    print(duel_trie[i][0][0],"contre",duel_trie[i][0][1],"gagne",duel_trie[i][1],"pts")

