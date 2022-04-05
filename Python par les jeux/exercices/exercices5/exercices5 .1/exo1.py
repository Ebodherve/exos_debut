from random import randint

l1 = list()
l2 = list()

for i in range(15) :
    l1.append(randint(1,10))

for i in l1 :
    if not (i in l2) :
        l2.append(i)

l2.sort()

print(l1)
print(l2)


