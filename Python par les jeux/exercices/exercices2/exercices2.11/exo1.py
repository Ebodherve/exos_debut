from random import randint

#données sur l'assaillant

arme_front_a = 0
arme_a = [0,0,0]    

#données sur le défenseur


arme_front_d = 0
arme_d = [0,0]


#données sur le combat
continu = True

while continu :
    
    nombre_arme_d = 3
    nombre_arme_a = 4
    territoire = input("territoire visée : ")

    #choix du nombre d'armées par l'attaquant
    while nombre_arme_a > 0 and nombre_arme_d > 0 :
        while True :
            try : 
                choix = int(input("nombre d'armée que tu engage : "))
                if choix > 3 and nombre_arme_a + arme_front_a >= 3 :
                    print("tu n'as droit qu'à 3 armées au plus sur tes (04) armées")
                elif choix > nombre_arme_a :
                    print("il ne te reste plus que : ",nombre_arme_a + arme_front_a)
                else :
                    break
            except ValueError :
                print("entrée un nombre valide ")

        arme_front_a = choix
        arme_front_d = randint(1,2)
        print("j'ai choisit, ",arme_front_d,"armées")
        
        #déroulement des combats
        input("tape sur (entrée) pour lancer les {} dées".format(arme_front_a))
        for i in range(arme_front_a) :
          arme_a[i] = randint(1,6)
          print(arme_a[i])

        print("lancer des defenseur du térritoire attaqué")  

        for i in range(arme_front_d) :
            arme_d[i] = randint(1,6)
            print(arme_d[i])

        print("Différents combats : ")  


        if arme_front_a > arme_front_d :
            for i in range(arme_front_d) :
                if arme_a[i] > arme_d[i]:
                    nombre_arme_d -= 1
                    arme_front_d -=1
                    print(arme_a[i], ' contre ', arme_d[i],"bataille gagneé, le territoire adverse a perdu une armée de défenseurs ")
                else :
                    nombre_arme_a -= 1
                    arme_front_a -= 1
                    print(arme_a[i], ' contre ', arme_d[i],"bataille perdue, tu a perdu une armée d'assaillants ")
        else :
            for i in range(arme_front_a) :
                if arme_a[i] > arme_d[i]:
                    nombre_arme_d -= 1
                    arme_front_d -=1
                    print(arme_a[i], ' contre ', arme_d[i],"bataille gagneé, le territoire adverse a perdu une armée de défenseurs ")
                else :
                    nombre_arme_a -= 1
                    arme_front_a -= 1
                    print(arme_a[i], ' contre ', arme_d[i],"bataille perdue, tu a perdu une armée d'assaillants ")


        input("Il te reste {} armées, tape sur (entrée) pour continuer".format(nombre_arme_a))
                
    if nombre_arme_a > 0 :
        if "oui" != input("Bravo vous avez gagner cette guerre, voulez vous continuer (si oui entrez 'oui')") :
            continu = False
    else :
        if "oui" != input("Vous avez perdu cette guerre, voulez vous continuer (si oui entrez 'oui')") :
            continu = False


    




