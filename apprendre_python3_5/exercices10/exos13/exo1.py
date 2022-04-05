
def estUneMaj(param):
    return "A"<=param<="Z" or param in ["É","Ê","Ë","È","Ÿ","Ô","Û","Î","Ṏ","Ï","Ä"]

def number_of_maj(phrase):
    nbr_maj = 0
    for car in phrase :
        if estUneMaj(car):
            nbr_maj += 1
    return nbr_maj

print(number_of_maj("Nombre de Caractere en Majuscule De NoTre TEXte"))