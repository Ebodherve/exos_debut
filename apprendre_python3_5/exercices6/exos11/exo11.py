
def pf_triangle(a,b,c) : 
    if a>0 and b>0 and c>0 :
        if a<b+c and b<c+a and c<a+b :
            return True
        else :
            return False
    return False

def pft_isocel(a,b,c) :
    if a>0 and b>0 and c>0 :
        if a == b or b == c or a == c :
            return True
        return False
    return False

def pft_equi(a,b,c) :
    if a>0 and b>0 and c>0 :
        if a == b and a == c :
            return True
        return False
    return False

def pft_rectangle(a,b,c) :
    if a>0 and b>0 and c>0 :
        if a > b and a > c :
            if a*a == b*b + c*c :
                return True
            return False
        elif b > a and b > c :
            if b*b == a*a + b*b :
                return True
            return False
        else :
            if c*c == a*a + b*b :
                return True
            return False
    return False



print("entrer trois valeurs : ")

a = float(input("valeur-1 : "))
b = float(input("valeur-2 : "))
c = float(input("valeur-3 : "))

if pf_triangle(a,b,c) :
    print(" il est possible de former un triangle ")
    if pft_equi(a,b,c) :
        print(" il est possible de former un triangle equilatérale ")
    elif pft_isocel(a,b,c) :
        print(" il est possible de former un triangle isocele ")
    elif pft_rectangle(a,b,c) :
        print(" il est possible de former un triangle rectangle ")
else :
    print(" il est impossible de former un triangle ")






