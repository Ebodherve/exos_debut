from random import randint

def lance_de(nb_lances) :
    for i in range(nb_lances) :
        print(randint(1,8), end = "")
        print(" ", end = "")
    
def main() :
    decision = input("Lancer de deux cent dés à huit faces o-oui et n-non : ")
    if decision == 'o' :
        lance_de(200)
        print(" ")
    else :
        print(" ")
        print("aucun lancés")



if __name__ == '__main__':
    main()
    
