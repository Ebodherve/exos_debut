
def maximum(a,b,c) :
    max = a
    if max < b :
        max = b
    if max < c :
        max = c
    return max

a = int(input("nombre -1 : "))
b = int(input("nombre -2 : "))
c = int(input("nombre -3 : "))

print("le maximum des trois est : ", maximum(a,b,c))
