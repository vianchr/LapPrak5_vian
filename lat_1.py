def perkalian(bil_1,bil_2):
    print (f"{bil_1}x{bil_2}",end="=")
    for i in range (1,bil_1):
        i=bil_2
        print(i,end="+")
    hasil=bil_1*bil_2
    print(bil_2,end="=")
    print(hasil)
bil_1=int(input("bilangan 1:"))
bil_2=int(input("bilangan 2:"))
perkalian(bil_1,bil_2)
        