

#fonction de conversion de celsius à farenheit
def conversion_f_c(cel) :
    return (9/5)*cel + 32

#fonction de conversion de farenheit à celsius 
def conversion_c_f(far) :
    return (5/9)*(far-32)

choix = input("conversion de celsius ('oui' pour celsius et autre entrée pour farenheit) : ")
temp = float(input("entrer votre temperature : "))

if choix == 'oui' :
    print("léquivalent de {} celsius en farenheit est {} ".format(temp,conversion_c_f(temp)))
else :
    print("léquivalent de {} farenheit en celsius est {} ".format(temp,conversion_f_c(temp)))
