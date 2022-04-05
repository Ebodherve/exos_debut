#-*- coding:Utf-8 -*- 
# encoding: UTF-8

def trouve(chaine,car):
    index = 0
    carac_search = chaine[0]
    while carac_search != car and index <len(chaine):
        index += 1
        carac_search = chaine[index]
    if carac_search != car :
        return None
    return index


print(trouve("bonjour, qui suis-je : "," "))
print(trouve("Juliette & Roméo", "&"))