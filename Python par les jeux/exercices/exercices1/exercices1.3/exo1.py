from random import choice

ens_carac = ["a","b","c",'e','d','g','f','h','1','2','3','4','5','6','7','8','9','0','i','j','k','l','m','n','p','o','q','r','s','t','u','v','w','x','y','z']
mot = ""
for i in range(8) :
    mot = mot + choice(ens_carac)

print("mot de passe à huit caractere : " + mot)




