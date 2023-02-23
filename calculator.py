# Python3 Simple Calculator
# Indonesian

# untuk operasi penjumlahan
def penjumlahan(x, y):
    return x + y

# untuk operasi pengurangan
def pengurangan(x, y):
    return x - y

# untuk operasi perkalian
def perkalian(x, y):
    return x * y

# untuk operasi pembagian
def pembagian(x, y):
    return x / y

print("Pilih Operasi yang diinginkan")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

while True:
    # ambil inputan dari user
    pilihan = input("Masukkan pilihan anda (1/2/3/4) : ")

    # cek apakah inputan dari user ada dalam pilihan
    if pilihan in ('1', '2', '3', '4'):
        try:
            # Jika pilihan benar, akan muncul inputan untuk angka pertama dan kedua
            angka1 = float(input("Masukkan angka pertama : "))
            angka2 = float(input("Masukkan angka kedua   : "))
        except ValueError:
            # Jika inputan salah, muncul pesan seperti di bawah
            print("Invalid Input ! Masukkan hanya Angka !")
            continue

    if pilihan == '1':
        print(angka1, "+", angka2, "=", penjumlahan(angka1, angka2))
    elif pilihan == '2':
        print(angka1, "-", angka2, "=", pengurangan(angka1, angka2))
    elif pilihan == '3':
        print(angka1, "*", angka2, "=", perkalian(angka1, angka2))
    elif pilihan == '4':
        print(angka1, "/", angka2, "=", pembagian(angka1, angka2))

    # cek apakah user ingin melakukan perhitungan lagi
    # jika user tidak ingin melakukan perhitungan lagi hentikan proses pengulangan
    kalkulasi_lagi = input("Apakah ingin melakukan perhitungan lagi? (Y/N) : ")
    if kalkulasi_lagi == "N" or kalkulasi_lagi == "n":
        break
    else:
        print("Invalid Input ! ")
