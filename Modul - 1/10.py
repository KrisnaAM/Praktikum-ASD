#Nomer 10           
def selesaikanABC(a,b,c) :
    res = 0
    res = (b**2) - (4*a*c)

    if res == 0 :
        print("Determinannya nol. Persamaan mempunyai satu akar kembar.")
    elif res > 0 :
        print("Determinannya positif. Persamaan mempunyai akar real dan berlainan.")
    elif res < 0 :
        print("Determinannya negatif. Persamaan tidak mempunyai akar real.")
