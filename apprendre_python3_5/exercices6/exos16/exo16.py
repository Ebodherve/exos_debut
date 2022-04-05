import math

d1 = d2 =0.05

force = ((6.67)*10000*1000)/(math.pow(10,11)*d1*d1)

for i in range(5) :
	print("pour d = ",d1,"m : la force vaut : ",force,"N")
	
	d2 = 2*d1
	force = (force*d1*d1)/(d2*d2)
	d1 = d2




