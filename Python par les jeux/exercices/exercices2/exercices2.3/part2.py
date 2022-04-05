
m = 2
while m <= 12 :
    print("table de multiplication de {:2d}".format(m))
    for i in range(12) :
        print("{:4d}x{:2d} = {:2d}".format(m,i,i*m))
    m += 1

