

def indexmax(serie):
    idmax = 0
    max = serie[0]
    i = 1
    while i<len(serie) :
        if serie[i] > max :
            max = serie[i]
            idmax = i
        i +=1
    return idmax

print(indexmax([5, 8, 2, 1, 9, 3, 6, 7])) 
    

