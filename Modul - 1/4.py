#Nomer 4
def rerata(x) :
    a = 0
    b = 0
    for i in x :
        a += 1
        b = b + i
        a = float(a)
        b = float(b)
    return(b/a)
