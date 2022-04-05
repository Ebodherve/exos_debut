
l_premier = [1]*1000
for i in range(2,len(l_premier)):
    j = i+1
    while j< 1000:
        if j%i == 0:
            l_premier[j] = 0
        j+=1

print("liste des nombres premiers inferieurs à 1000: ")

for i in range(2,len(l_premier)):
    if l_premier[i] == 1 :
        print(i)

