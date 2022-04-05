nele = npb = 0
nbnote = snote = mnote = 0

note = float(input("entrer une note d'élève : "))
nele = npb = note
nbnote = 1
snote = mnote = note

while note >= 0 :
	print("nombre de notes entrer : ",nbnote)
	print("note la plus élevé : ", nele)
	print("note la plus basse : ", npb)
	print("moyenne des notes : ", mnote)
	
	note = float(input("entrer une nouvelle note : "))
	
	if note > nele :
		nele = note
	elif note < npb :
		npb = note
	
	nbnote += 1
	snote += note
	mnote = snote/nbnote



