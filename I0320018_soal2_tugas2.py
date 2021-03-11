# membuat variabel
nama = "Bonang Respati Satmoko"
tinggi = 166
berat = 68.8
sepatu = 43
alamat = "Tangerang Selatan, Banten, Indonesia"

# bulan dan tahun lahir
bulanLahir = 3           # 3 = Maret
tahunLahir = 2002

# bulan dan tahun sekarang
bulanNow = 3             # 3 = Maret
tahunNow = 2021

# menghitung jumlah bulan
jumlahBulanLahir = 12 * tahunLahir + bulanLahir  # 12 = jumlah bulan tiap tahun
jumlahBulanNow = 12 * tahunNow + bulanNow        # 12 = jumlah bulan tiap tahun

# menghitung usia dalam satuan bulan
usiaDalamBulan = jumlahBulanNow - jumlahBulanLahir

# mengubah satuan bulan ke satuan XX tahun XX bulan
usiaTahun = int(usiaDalamBulan/12)               # int digunakan untuk menghilangkan desimal
usiaBulan = usiaDalamBulan % 12                  # operasi % akan menghasilkan sisa dalam satuan bulan

# memasukkan usia ke dalam variabel
usia = str(usiaTahun) + " Tahun " + str(usiaBulan) + " Bulan"

#tampilan
print("===== Biodata =====")
print("Nama lengkap   :", nama)
print("Usia           :", usia)
print("Tinggi badan   :", tinggi)
print("Berat  badan   :", berat)
print("Tempat tinggal :", alamat)
print("Ukuran sepatu  :", sepatu)
