

def change_cle_val_dic(e_c_v) :
    for i,j in e_c_v.items() :
        e_c_v.pop(i)
        e_c_v[j] = i

dic = {"bon" : "good","mauvais":"bad","etre":"to be"}
print(dic)
change_cle_val_dic(dic)
print(dic)