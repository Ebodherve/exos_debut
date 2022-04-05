t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
t2 = [ ' Janvier ' , ' Février ' , ' Mars ' , ' Avril ' , ' Mai ' , ' Juin ' ,' Juillet ' , 
      ' Août ' , ' Septembre ' , ' Octobre ' , ' Novembre ' , ' Décembre ' ]

print(t2)

id_insertion = 1

for ele in t1:
    t2[id_insertion:id_insertion] = [ele]
    id_insertion += 2

print(t2)