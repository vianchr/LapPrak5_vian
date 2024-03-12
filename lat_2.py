def ganjil(bawah,atas):
    if bawah>atas:
        for i in range(bawah,atas-1,-1):
            if i%2!=0:
                if i!=atas and i!=atas+1:
                    print(i,end=",")
                else:
                    print(i,end=".")                  
    else:
        for i in range(bawah,atas+1):
            if i%2!=0:
                if i!=atas and i!=atas-1:
                    print(i,end=",")
                else:
                    print(i,end=".")
                
bawah=int(input("batas bawah:"))
atas=int(input("batas atas:"))
ganjil(bawah,atas)