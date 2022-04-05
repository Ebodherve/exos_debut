
def volBoite(x1 = -1,x2 = -1,x3 = -1) :
    
    if x1>=0 and x2>=0 and x3>=0 :
        return x1*x2*x3
    elif x1>=0 and x2>=0 and x3<0 :
        return x1*x2
    elif x1>=0 and x2<=0 and x3<0:
        return x1
    elif x1<0 and x2>=0 and x3>=0 :
        return x2*x3
    elif x1<0 and x2>=0 and x3<0 :  
        return x2
    elif x1>=0 and x2<0 and x3>=0 :
        return x1*x3
    elif x1<0 and x2<0 and x3>=0 :
        return x3
    else :
        return -1
    

print(volBoite())
print(volBoite(5.2))
print(volBoite(5.2,3))
print(volBoite(5.2,3,7.4))


