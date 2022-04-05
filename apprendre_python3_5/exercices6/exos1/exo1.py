
def vitesse(vit):
    v = []
    v.append(vit*1609/3600)
    v.append(vit*1.609)
    return v

v = float(input("entrez la vitesse en mile/h : "))
lv = vitesse(v)
print("vitesse en m/s : ",lv[0])
print("vitesse en km/h : ",lv[1])


