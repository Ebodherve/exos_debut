from os import chdir

chdir("/home/tsanga/Bureau/CONSERVE/conserve2/programmation/apprentissage/python/apprendre_python3_5/exercices9/exos7")

def copy_l1_l2(a = "a",b = "b",c = "c"):
    fa = open(a,"r")
    fb = open(b,"r")
    fc = open(c,"a")
    
    la = fa.readlines()
    lb = fb.readlines()
    fa.close()
    fb.close()

    i = 0
    na = len(la)
    nb = len(lb)
    if na<nb :
        while i<na :
            fc.write(la[i])
            fc.write(lb[i])
            i += 1
        for l in lb[i:] :
            fc.write(l)
    else :
        while i<nb :
            fc.write(la[i])
            fc.write(lb[i])
            i += 1
        for l in la[i:] :
            fc.write(l)

copy_l1_l2()