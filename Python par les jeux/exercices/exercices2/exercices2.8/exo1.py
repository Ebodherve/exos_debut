from random import random



nl = ne = nr = nc = 0
n_pack_nvalide = 0
pacr = ["1","2","1","1","2"]

#lpacr = []

npacr = int(input("nombre de packet de 05 cartes : "))
if npacr < 0 :
    npacr = -1 * npacr

for i in range(npacr) :
    
    
    for j in range(5) :
        rnd = random()

        if rnd < 0.01:
            pacr[j] = "L"
        elif rnd < 0.04:
            pacr[j] = "E"
        elif rnd < 0.23 :
            pacr[j] = "R"
        else :
            pacr[j] = "C"


    est_pac = False

    carte1 = pacr[0]
    
    legendaire_present = (carte1 == "L")

    for carte in pacr :
        if carte == "L" :
            legendaire_present = True
        if carte1 != carte :
            est_pac = True
        carte1 = carte

    if est_pac :
        for carte in pacr :
            if carte == "L" :
                nl += 1
            elif carte == 'E' :
                ne += 1
            elif carte == "R" :
                nr += 1
            else :
                nc += 1

    else :
        n_pack_nvalide += 5

    if est_pac :
        if legendaire_present :
            print(pacr," ! ")
        else :
            print(pacr)
        
    else:
        print(pacr," : pacquet de cartes non valide")
        

print("")
nom_t_c = 5 * npacr - n_pack_nvalide
if nom_t_c != 0 :
    print(nl," légendaire(s) : ",(nl/nom_t_c)*100,"%")
    print(ne," épique(s) : ",(ne/nom_t_c)*100,"%")
    print(nr," rare(s) : ",(nr/nom_t_c)*100,"%")
    print(nc," commune(s) : ",(nc/nom_t_c)*100,"%")






