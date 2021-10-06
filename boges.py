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
'''
def adalah function yang menerima 3 argument yaitu input dengan tipe data
number integer.
kemudian argument tersebut akan diperiksa oleh pengkondisian
if else didalam function kalkulator menggunakan operator perbandingan
apabila input sesuai/true dengan salah satu kondisi maka lakukan operasi
menggunakan operator aritmatika lalu return hasilnya.
'''
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
