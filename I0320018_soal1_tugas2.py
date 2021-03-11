### Menghitung luas persegi panjang

# informasi program
print("===== Menghitung luas persegi panjang =====")

# input panjang dan lebar
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

# proses hitung luas
luasPersegiPanjang = panjang * lebar

# menampilkan hasil
print("Luas persegi panjang =", luasPersegiPanjang, "\n")

### Menghitung luas lingkaran

# informasi program
print("===== Menghitung luas lingkaran =====")

# input jari-jari
r = float(input("Masukkan jari-jari: "))

# proses hitung luas

luasLingkaran = 3.14 * (r ** 2)

# menampilkan hasil
print("Luas lingkaran =", luasLingkaran, "\n")

### Menghitung luas kubus

# informasi program
print("===== Menghitung luas kubus =====")

# input rusuk
s = float(input("Masukkan panjang rusuk: "))

# proses hitung luas
luasKubus = 6 * (s ** 2)

# menampilkan hasil
print("Luas kubus =", luasKubus, "\n")

### Menghitung konversi suhu celcius ke fahrenheit

# informasi program
print("===== Konversi suhu celcius ke fahrenheit =====")

# input celcius
celcius = float(input("Masukkan suhu celcius: "))

# proses hitung celcius ke fahrenheit
fahrenheit = (celcius * (9/5))+ 32

# menampilkan hasil
print(celcius, "celcius =", fahrenheit, "fahrenheit", "\n")

### Menghitung konversi suhu reamur ke kelvin

# informasi program
print("===== Konversi suhu reamur ke kelvin =====")

# input reamur
reamur = float(input("Masukkan suhu reamur: "))

# proses hitung celcius ke fahrenheit
kelvin = (reamur * (5/4)) + 273.15

# menampilkan hasil
print(reamur, "reamur =", kelvin, "kelvin")
