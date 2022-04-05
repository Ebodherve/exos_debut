#fonction qui verifie si un caratere est une voyelle ou pas
def voyelles(car):
    return car in ["e","o","a","u","i","y"] or chr(ord(car)+32) in ["e","o","a","u","i","y"]

