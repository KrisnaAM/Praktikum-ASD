#Nomer 6
def cekPrima() :
    y = range(1001)
    for i in range(2,1001) :
        x = 0
        for j in range(i) :
            if i % (j+1) == 0 :
                x += 1
        if x == 2 :
            print(i)
