#Nomer 5
def apakahPrima(a) :
    x = 0
    for i in range(a) :
        if a % (i+1) == 0 :
            x += 1
    if x == 2 :
        print("YA")
    else :
        print("TIDAK")
