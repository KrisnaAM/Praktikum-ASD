#Nomer 11
def apakahKabisat() :
    thn = int(input("Masukkan Tahun : "))
    if thn % 4 == 0 :
        if thn % 100 == 0 :
            if thn % 400 == 0 :
                print (True)
            else :
                print (False)
        else :
            print (True)
    else :
        print (False)
