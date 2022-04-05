#module de conservation et d'extraction de variables avec leurs types

#fonction de conseravtion
"""def conserve_vtype(file,variable) :
    if type(variable) == "<class 'int'>":
        file.write("<class 'int'>"+str(variable)+"\n")
    elif type(variable) == "<class 'float'>":
        file.write("<class 'float'>"+str(variable)+"\n")
    elif type(variable) == "<class 'str'>":
        file.write("<class 'str'>"+str(variable)+"\n")"""

def conserve_vtype(file,variable) :
    file.write(str(type(variable))+str(variable)+"\n")

#fonction extract variable type
def var_type(file):
    line = file.readline()
    type_v = line[0]
    char = line[1]
    i = 2
    while char != '>':
        type_v += char
        char = line[i]
        i += 1
    if type_v == "<class 'int'>":
        return int(line[i:])
    elif type_v == "<class 'float'>":
        return float(line[i:])    
    elif type_v == "<class 'str'>":
        return str(line[i:])
