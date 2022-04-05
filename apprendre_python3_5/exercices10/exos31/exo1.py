def copie_sans_doublons(liste):
    l_ret = []
    for i in liste:
        if i not in l_ret:
            l_ret.append(i)
    return l_ret

l1 = [45,45,1,3,1,45,65,21,98,47,21,12,12,13,21]
print(l1)
print(copie_sans_doublons(l1))
