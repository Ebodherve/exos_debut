

def elemax(liste,debut = 0,fin = -1):
    fin = len(liste)
    max = liste[debut]
    for i in liste[debut:fin]:
        if i>max :
            max = i
    return max
            
    
print(elemax([9, 3, 6, 1, 7, 5, 4, 8, 2,12]))
