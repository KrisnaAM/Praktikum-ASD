#Nomer 7
def faktorPrima(x):
    listprima=[]
    prima=2
    while prima<=x:
        if x%prima==0:
            x/=prima
            listprima.append(prima)
        else:
            prima+=1
    return listprima
