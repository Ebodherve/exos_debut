

def dechiffre(mcrip) :
    eldecriptage = {"W":"A", "B":"B", "H":"C", "A":"D", "Y":"E", "P":"F", "O":"G", "D":"H", "Q":"I", "Z":"J", "X":"K", "N":"L", "T":"M", "S":"N", "F":"O", "L":"P", "R":"Q", "U":"R", "V":"S", "M":"T", "C":"U", "E":"V", "K":"W", "J":"X", "G":"Y", "I":"Z"}
    car_dechif = ""
    for car in mcrip :
        car_dechif += eldecriptage[car]
        
    return car_dechif

car_chif = "HYHQYVMCSHDQPPUYAYVCBVMQMCMQFS"       
print(car_chif)
print(dechiffre(car_chif))