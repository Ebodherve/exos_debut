def table(n) :
    i = 0
    while i < 12 :
        print("{:4d}x{:2d} = {:2d}".format(n,i,i*n))
        i += 1

m = 2
while m <= 12 :
    print("table de multiplication de {:2d}".format(m))
    table(m)        
    m += 1
