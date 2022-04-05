

def compteCar(ca,ch) :
    tch = len(ca)
    i = 0
    nca = 0
    while i<=len(ch) : 
        if ca == ch[i:i+tch] :
            nca += tch
        i += tch
    return nca

print(compteCar('e','Cette phrase est un exemple'))


