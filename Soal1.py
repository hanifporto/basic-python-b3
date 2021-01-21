
import array
print ("Selamat datang")



print ("--- Menu --- ")
print ("1. Daftar Kontak 2. Tambah Kontak 3. Keluar")

A = int(input('Masukan Menu :'))

#daftar_kontak = ("Nama : Nafi", "No Telepon : 08123456789", "Nama  : Joko", "No Telepon : 028987654321")

nama = ["Nafi","Joko"]
no_telepon = ["08123456789","028987654321"]

B = (nama[0],no_telepon[0],nama[1],no_telepon[1])
if (A == 1):
    print (B)
else :
    print ("Menu tidak tersedia") 
if (A== 2):
    (nama.append(input("Nama:")))
    (no_telepon.append(input("Nomor Telepon:")))
    print("kontak sudah berhasil ditambahkan")
if (A== 3) :
    print ("Program selesai, sampai jumpa!")


