from math import sqrt

class Point(object):
    "définition d'un point"


def distance_p(a,b):
    return sqrt((a.x-b.x)**2 + (a.y-b.y)**2)


p1 = Point()
p1.x = 12
p1.y = 45

p2 = Point()
p2.x = 42
p2.y = 10

print(distance_p(p1,p2))
