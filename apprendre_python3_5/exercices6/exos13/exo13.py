
gnote = int(input("entrer la plus grande note que l'on peut avoir dans une matiere : "))
note = int(input("entrer votre note dans cette matiere : "))

pc = (note/gnote)*100

if pc >= 80 :
	print("vous avez un A")
elif pc >= 60:
	print("vous avez un B")
elif pc >= 50:
	print("vous avez un C")
elif pc >= 40:
	print("vous avez un D")
else:
	print("vous avez un E")

	 
	



