
def changeCar(ch,ca1,ca2,debut=0,fin=-1) :
    ec =  len(ca1)
    fin = len(ch)
    for i in range(debut,fin-1,ec) :
        if ch[i:ec+i] == ca1 :
            ch = ch[:i]+ca2+ch[i+ec:]
    return ch

phrase = "bonjour à tout le monde du python3.8 comment allez vous ?"
print(changeCar(phrase,'to','z'))
        
    

