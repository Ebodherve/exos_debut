


def est_bisect(ann) :
    if (ann%4 == 0 and ann%100 != 0) or ann%400 == 0 :
        return True
    return False



a = int(input('année : '))

if est_bisect(a) : 
    print("Année bissectile")
else :
    print("Année non bissectile")


