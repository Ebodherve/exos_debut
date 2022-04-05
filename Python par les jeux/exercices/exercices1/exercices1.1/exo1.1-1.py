from random import randint

def lance_de(nb_lances) :
    for i in range(nb_lances) :
        print(randint(1,6), end = "")
        print(" ", end = "")
    
def main() :
    decision = input("Lancer de trois dés à six faces 3-oui et n-non : ")
    if decision == '3' :
        lance_de(3)
        print(" ")
    else :
        print("aucun lancés")



if __name__ == '__main__':
    main()
    
