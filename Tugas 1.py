def penjumlahan(a,b,c):
    penjumlahan = float(a) + float(b) + float(c)
    return penjumlahan
def pengurangan(a,b,c):
    pengurangan = float(a) - float(b) - float(c)
    return pengurangan
def perkalian(a,b,c):
    perkalian = float(a) * float(b) * float(c)
    return perkalian
def pembagian(a,b,c):
    pembagian = float(a) / float(b) / float(c)
    return pembagian

ulang = 'y'
while ulang == 'y':
    a = input('Masukkan Bilangan 1: ')
    b = input('Masukkan Bilangan 2: ')
    c = input('Masukkan Bilangan 3: ')
    print(' 1.penjumlahan \n 2.pengurangan \n 3.perkalian \n 4.pembagian \n')
    d = input('Pilih 1-4 : ')
    if d == '1':
        print(' Hasilnya adalah = ', penjumlahan(a,b,c))
    if d == '2':
        print(' Hasilnya adalah = ', pengurangan(a,b,c))
    if d == '3':
        print(' Hasilnya adalah = ', perkalian(a,b,c))
    if d == '4':
        print(' Hasilnya adalah = ', pembagian(a,b,c))
    ulang = input("Coba lagi ? [y/t] : ")