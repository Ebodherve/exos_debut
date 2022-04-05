from  random import choice,randint,shuffle

from tkinter import *

"""
mat_bin = [[False,False,False,False,True,True,True,True,True] for i in range(3)]
mat_nom = [[-1,-1,-1,-1,-1,-1,-1,-1,-1] for i in range(3)]
"""

mat_bin = [[False]*4 + [True]*5 for i in range(3)]
mat_nom = [[-1]*9 for i in range(3)]

ncv = []
ncf = []
nc1v = []
nc2v = []

#mettre en desordre les elements de chaque ligne de la matrice
def derange_ligne() :
    shuffle(mat_bin[0])
    shuffle(mat_bin[1])
    shuffle(mat_bin[2])

def est_afalse_col(i) :
    if mat_bin[0][i] == True :
        return False
    elif mat_bin[1][i] == True :
        return False
    elif mat_bin[2][i] == True :
        return False
    return True

def est_atrue_col(i) :
    if mat_bin[0][i] == False :
        return False
    elif mat_bin[1][i] == False :
        return False
    elif mat_bin[2][i] == False :
        return False
    return True

def a2_cel_false_col(i) :
    nbf = 0
    for li in range(3) :
        if mat_bin[li][i] == False :
            nbf += 1
    if nbf == 2 :
        return True
    return False

def a2_cel_true_col(i) :
    nbf = 0
    for li in range(3) :
        if mat_bin[li][i] == True :
            nbf += 1
    if nbf == 2 :
        return True
    return False

#lister les indices de colones ayant toutes les cases à true
def lindice_col_true() :
    for i in range(8) :
        if est_atrue_col(i) :
            ncv.append(i)

#lister les indices de colones ayant 2 cases à true
def lindice_col_2true() :
    for i in range(8) :
        if a2_cel_true_col(i) :
            nc2v.append(i)

#lister les indices de colones ayant 2 cases à false
def lindice_col_2false() :
    for i in range(8) :
        if a2_cel_false_col(i) :
            nc1v.append(i)
#lister les indices de colones ayant toutes les cases à false
def lindice_col_false() :
    for i in range(8) :
        if est_afalse_col(i) :
            ncf.append(i)
# returne la liste des indices de ligne false, de la colone col
def l_indligne_false(col) :
    lind = []
    for i in range(3) :
        if mat_bin[i][col] == False :
            lind.append(i)
    return lind

#retourne la liste des indices de ligne true, de la colone col
def l_indligne_true(col) :
    lind = []
    for i in range(3) :
        if mat_bin[i][col] == True :
            lind.append(i)
    return lind
            
#permute 2 cellules de la ligne li des 2 colones coli et colj
def permute(coli,colj,li) :
    per = mat_bin[li][coli]
    mat_bin[li][coli] = mat_bin[li][colj]
    mat_bin[li][colj] = per

#permutation d'1 ou de 2 d'une cellule colone à true dans avec 1 ou 2 colone à false
def permute_true_false(t,f) :
    nbpermutation = randint(1,2)
    l_indice_p = [0,1,2]
    l_indice = []
    for i in range(nbpermutation) :
        choix = choice(l_indice_p)
        l_indice.append(choix)
        l_indice_p.remove(choix)
        
    for i in l_indice :
        permute(t,f,i)

#arrangement des cases de la matrice binaire correspondant à la carte de loto
def arrangement_mb() :
    derange_ligne()
    if est_afalse_col(8)  :
        choix_ligne = choice([0,1,2])
        shuffle(mat_bin[choix_ligne])
        if mat_bin[choix_ligne][8] == False :
            i = 0
            while mat_bin[choix_ligne][i] != True :
                i += 1
            permute(i,8,choix_ligne)
    lindice_col_true()
    lindice_col_false()
    if len(ncv) > len(ncf) :
        j = 0
        for i in ncf :
            permute_true_false(i,ncv[j])
            j += 1
        lindice_col_2false()
        shuffle(nc1v)
        k = 0
        for i in ncv[j:] :
            permute(i,nc1v[k],choice(l_indligne_false(nc1v[k])))
            k += 1
    elif len(ncf) > len(ncv) :
        j = 0
        for i in ncv :
            permute_true_false(i,ncf[j])
            j += 1
        lindice_col_2true()
        shuffle(nc2v)
        k = 0
        for i in ncf[j:] :
            permute(i,nc2v[k],choice(l_indligne_true(nc2v[k])))
            k += 1
    else :
        j = 0
        for i in ncf :
            permute_true_false(i,ncv[j])
            j += 1
    
#generation de la marice de nombres
def generation_mat_nbr() :
    lcol = [i for i in range(80,90,1)]
    #colone 8
    for i in range(3) :
        if mat_bin[i][8] == True :
            choix = choice(lcol)
            mat_nom[i][8] = choix
            lcol.append(choix)
    ecart = 9
    pval = 1
    dval = 9
    for j in range(8) :
        lcol = [i for i in range(pval,dval,1)]
        #colone j
        for i in range(3) :
            if mat_bin[i][j] == True :
                choix = choice(lcol)
                mat_nom[i][j] = choix
                lcol.append(choix)
        pval = dval + 1
        dval = pval + ecart


#construction grphique de la carte
def contruction_gui() :
    arrangement_mb()
    generation_mat_nbr()
    
    indligne = 0
    
    for i in mat_nom :
        indcolone = 0
        for j in i :
            if j == -1 :
                b = Button(fen,bg = 'black',text = " ")
                b.grid(row = indligne,column = indcolone)
            else :
                b = Button(fen,bg = 'white',text = str(j))
                b.grid(row = indligne,column = indcolone)
            indcolone += 1
        indligne +=1



# prgramme principale
fen = Tk()
contruction_gui()
"""print(mat_nom[0])
print(mat_nom[1])
print(mat_nom[2])"""

fen.mainloop()


