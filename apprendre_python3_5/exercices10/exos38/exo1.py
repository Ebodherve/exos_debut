
A = [45,87,65,32,15,47,85,95]

i=0
B = [0]*len(A)
B[:] = A

A[0] = 789
B[0] = 4648

print(A)
print(B)