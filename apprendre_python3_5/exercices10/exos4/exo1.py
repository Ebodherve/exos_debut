# encoding: UTF-8

def trouve(chaine,car,find):
    index = find
    carac_search = chaine[0]
    while carac_search != car and index <len(chaine):
        index += 1
        carac_search = chaine[index]
    if carac_search != car :
        return None
    return index
print(trouve ("César & Cléopâtre", "r", 5))