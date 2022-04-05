from random import shuffle


lic = ['Wade Barrett'," Daniel Bryan", "Sin Cara", "John Cena", "Antonio Cesaro", "Brodus Clay", "Bo Dallas", "The\
Godfather", "Goldust", "Kane", "The Great Khali", "Chris Jericho", "Kofi Kingston", "Jinder Mahal", "Santino\
Marella", "Drew McIntyre", "The Miz", "Rey Mysterio", "Titus O'Neil", "Randy Orton", "David Otunga", "Cody\
Rhodes", "Ryback", "Zack Ryder", "Damien Sandow", "Heath Slater", "Sheamus", "Tensai", "Darren Young", "Dolph\
Ziggle "]

taille = len(lic)

print("liste des cactheurs")
for i in range(taille-1) :
    print(lic[i],',', end = "")

print(lic[taille-1])

shuffle(lic)

print("")
print("orde d'entrée des cactheurs : ")
print("")

for i in range(taille-1) :
    print(lic[i])

print(lic[taille-1])



