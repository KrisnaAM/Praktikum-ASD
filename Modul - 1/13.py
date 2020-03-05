#Nomer 13
def katakan(x):
    satuan = [' ', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh', 'sebelas']
    hasil = ""
    if x <= 0:
        hasil += 'Bilangan Haruslah Positif\ndan Bilangan Asli'
    elif x < 12 :
        hasil += satuan[x]
    elif x < 20 :
        hasil += katakan(x-10) + " belas "
    elif x < 100:
        hasil += katakan(int(x/10)) + " puluh " + katakan(x%10)
    elif x < 200 :
        hasil += "seratus " + katakan(x-100)
    elif x < 1000 :
        hasil += katakan(int(x/100)) + " ratus " + katakan(x%100)
    elif x < 2000 :
        hasil += "seribu " + katakan(x-1000)
    elif x < 1000000 :
        hasil += katakan(int(x/1000)) + " ribu " + katakan(x%1000)
    elif x < 1000000000 :
        hasil += katakan(int(x/1000000)) + " juta " + katakan(x%1000000)
    elif x >= 1000000000 :
        hasil += katakan(int(x/1000000000)) + " milyar " + katakan(x%1000000000)
    return hasil
