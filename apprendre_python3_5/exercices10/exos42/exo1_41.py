from random import *

def list_aleat(n):
    s = []
    for i in range(n):
        s.append(random())
    return s

print(list_aleat(8))