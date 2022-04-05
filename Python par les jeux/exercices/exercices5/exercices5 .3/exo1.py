from math import sqrt 

n = 1000

l1 = [1]*(n+1)

l1[0],l1[1] = 0,0

np = 0

for i in range(2,int(sqrt(n)),1) :
    for j in range(i+1,n+1,1) :
        if(j%i == 0 and l1[j] == 1) :
            l1[j] = 0
        #np += 1

np = 0

for i in l1 :
    if i==1 :
        print(np)
    np += 1


