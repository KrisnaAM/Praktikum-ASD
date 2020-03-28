class Mahasiswa(object):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        
def BubbleSort(val):
    for passnum in range(len(val)-1,0,-1):
        for i in range(passnum):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp

        
c0 = Mahasiswa('Krisna',10,'Sragen',300000)
c1 = Mahasiswa('Ganta',51,'Surabaya',330000)
c2 = Mahasiswa('Ricky',2,'Madiun',280000)
c3 = Mahasiswa('Anom',18,'Surakarta',237000)
c4 = Mahasiswa('Juandru',4,'Semarang',670000)
c5 = Mahasiswa('Deli',31,'Salatiga',250000)
c6 = Mahasiswa('Hanif',13,'Malang',245000)
c7 = Mahasiswa('Faisal',5,'Wonogiri',245000)
c8 = Mahasiswa('Jason',23,'Depok',245000)
c9 = Mahasiswa('Jaya',64,'Pekalongan',270000)
c10 = Mahasiswa('Aprillia',29,'Yogyakarta',230000)

angka = [c0.NIM,c1.NIM,c2.NIM,c3.NIM,c4.NIM,c5.NIM,c6.NIM,c7.NIM,c8.NIM,c9.NIM,c10.NIM]
BubbleSort(angka)
print(angka)
