def penjumlah(n):
    if n <= 1:
        return n
    else:
        return n + penjumlah(n-1)
 
bil = int(input('input bilangan : '))
 
if bil < 0:
    print('Masukkan bilangan positif')
else:
    print('Penjumlahan dari nilai asli', bil,'adalah',penjumlah(bil))
