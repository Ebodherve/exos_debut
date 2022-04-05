from random import choice

def lance_de(nb_lances) :
        dee = [1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,6,6,6]
        for i in range(nb_lances) :
                print(choice(dee), end = "")
                print(" ", end = "")
    
def main() :
    decision = input("Lancer d'un dé pipé à six faces o-oui et n-non : ")
    if decision == 'o' :
        lance_de(1)
        print(" ")
    else :
        print(" ")
        print("aucun lancés")



if __name__ == '__main__':
    main()
    




