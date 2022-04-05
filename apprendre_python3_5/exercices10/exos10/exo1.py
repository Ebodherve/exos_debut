
def estUneMaj(param):
    return "A"<=param<="Z" or param in ["É","Ê","Ë","È","Ÿ","Ô","Û","Î","Ṏ","Ï","Ä"]

print(estUneMaj("4"))
print(estUneMaj("Q"))