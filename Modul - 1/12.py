#Nomer 12
def tebak() :
    a = random.randrange(1,101)
    b = -1
    n = 0
    print("Permainan tebak angkat.")
    print("Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak")
    while a != b :
        n = n + 1
        b= int(input("Masukkan tebakan ke-"+str(n)+":> "))
        if b < a :
            print("Itu terlalu kecil. Coba lagi")
        elif b > a :
            print("Itu terlalu besar. Coba lagi")
        else :
            print("Ya. Anda benar.")
            break
