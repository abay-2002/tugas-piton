#Akbar Angkasa 32220036
#TUGAS PRAKTIKUM 3
'''
1. Buatlah program menggunakan pernyataan if
untuk menentukan besarnya potongan/diskon harga
yang diterima oleh pembeli, berdasarkan kriteria:
√ tidak ada potongan/diskon harga
jika total pembelian kurang dari Rp. 100.000
(dalam hal ini potongan harga diinisialisasi dengan nol).
√ bila total pembelian lebih dari atau sama dengan Rp. 100.000,
potongan/diskon harga yang diterima sebesar 5% dari total pembelian.
Contoh Jalannya Program:
Total pembelian = 50.000 <enter>
Total yang harus dibayar adalah Rp.50.000
Contoh Jalannya Program:
Total pembelian = 100.000 <enter>
Total yang harus dibayar adalah Rp.95.000
'''
print("Akbar Angkasa 3220036")
print("nomor 1")
from decimal import *
totalPembelian = int(input("masukan total pembelian:"))
if totalPembelian < 100000:
    print("Total yang harus dibayar adalah", totalPembelian)
elif totalPembelian >= 100000:
    hargaFix = totalPembelian * float(0.05)
    potonganHarga = totalPembelian - hargaFix
    print("Total yang harus dibayar adalah Rp.",int(potonganHarga) )
else:
    print("masukan nilai")


'''
2. Modifikasi program sebelumnya dengan menggunakan pernyataan if else
untuk menentukan besarnya potongan/diskon harga
yang diterima oleh pembeli dan menampilkan besaran diskon yang diperoleh,
berdasarkan kriteria:
√ tidak ada potongan/diskon harga
jika total pembelian kurang dari Rp. 100.000
(dalam hal ini potongan harga diinisialisasi dengan nol).
√ bila total pembelian lebih dari atau sama dengan Rp. 100.000,
potongan/diskon harga yang diterima sebesar 5% dari total pembelian.
√ output program akan menampilkan besaran diskon dan total pembayaran.
Contoh Jalannya Program:
Total pembelian = 50.000 <enter>
Anda Tidak mendapat diskon
Total yang harus dibayar adalah Rp.50.000

Contoh Jalannya Program:
Total pembelian = 100.000 <enter>
Anda mendapat diskon sebesar Rp. 5.000
Total yang harus dibayar adalah Rp.95.000
'''
print("nomor 2")
print("Akbar Angkasa 3220036")
totalBelanja = int(input("masukan total pembelian:"))
if totalBelanja < 100000:
    print("Anda Tidak mendapat diskon")
elif totalBelanja >= 100000:
    hargaFix = totalPembelian * float(0.05)
    potonganHarga = totalPembelian - hargaFix
    print("anda mendapat diskon sebesar ", int(hargaFix), "total yang harus dibayar adalah ",int(potonganHarga))
else:
    print("masukan harga")

'''
3. Dengan menggunakan pernyataan else.. if, buatlah program kalkulator sederhana, untuk mendapatkan tampilan hasil sebagai berikut:
masukkan bilangan pertama : 5 <enter>
masukkan bilangan kedua : 3 <enter>
Menu Matematika
1. Penjumlahan
2. Pengurangan
3. Pembagian
4. Perkalian
Masukkan Pilihan Anda : 4 <enter>
Hasil operasi tersebut = 15
'''
print("nomor 3")
print("Akbar Angkasa 3220036")
def kalkulator(a,b,pilihan):
    if pilihan == 1:
        total = a + b
        return total
    elif pilihan == 2:
        total = a - b
        return total
    elif pilihan == 3:
        total = a // b
        return total
    elif pilihan == 4:
        total = a * b
        return total
    else:
        return print("masukan nilai")

a = int(input("masukan bilangan pertama"))
b = int(input("masukan bilangan kedua"))
pilihan = int(input("masukan operasi matematika \n"
           "1.penjumlahan \n"
           "2.pengurangan \n"
           "3.pembagian \n"
           "4.perkalian \n"
           "Operasi = "
          ))
inputUser = kalkulator(a,b,pilihan)
print("hasil operasi tersebut = ", inputUser)

        
    
    





