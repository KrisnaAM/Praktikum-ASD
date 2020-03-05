#Nomer 14           
def formatRupiah(a) :
    a = list(str(a))
    b = len(a)
    if b % 3 == 0 :
        b = int(b/3) - 1
    else :
        b = int(b/3)
    n = 0
    for i in range(b) :
        x = -3*(i+1)
        a.insert(int(x)+n,".")
        n = n - 1
    a = "".join(a)
    print("Rp "+a)
       
