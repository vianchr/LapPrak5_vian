def ips():
    juMat=int(input("total matakuliah:"))
    i=0
    rata_rata=0
    while i<juMat:
        huruf=input(f"nilai MK {i+1} :")
        if huruf=="A":
            angka=4
        elif huruf=="B":
            angka=3
        elif huruf=="C":
            angka=2
        elif huruf=="D":
            angka=1
        rata_rata=rata_rata+angka
        i+=1
    
    return round(rata_rata/i,2)
total=ips()
print(f"rata ratanya adalah {total}")