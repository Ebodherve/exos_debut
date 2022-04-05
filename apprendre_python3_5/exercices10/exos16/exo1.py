
def convert_caract(phrase):
    phrase_ret = ""
#    cadeplace = ""
    for car in phrase :
        if "A"<= car <="Z":
            phrase_ret += chr(ord(car)+32)
        elif "a"<= car <="z":
            phrase_ret += chr(ord(car)-32)
        elif "À"<= car <="Ý":
            phrase_ret += chr(ord(car)+32)
        elif "à"<= car <="ÿ":
            phrase_ret += chr(ord(car)-32)
        else :
            phrase_ret += car
    return phrase_ret


print(convert_caract("bonJour à tous ce Qui REgearde ce script PythOn 3:"))
