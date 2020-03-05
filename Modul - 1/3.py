#A
def jumlahhurufvokal(x):
    vokal="AIUEOaiueo"
    jmlhuruf=len(x)
    jmlvokal=0
    for karakter in x:
        if karakter in vokal:
            jmlvokal+=1
    return (jmlhuruf, jmlvokal)
k=jumlahhurufvokal("Surakarta")
print(k)

#B
def jumlahhurufkonsonan(x):
    konsonan="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    jmlhuruf=len(x)
    jmlkonsonan=0
    for karakter in x:
        if karakter in konsonan:
            jmlkonsonan+=1
    return (jmlhuruf, jmlkonsonan)
k=jumlahhurufkonsonan("Surakarta")
print(k)


