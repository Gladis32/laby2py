# Input nilai variable
a = input("Masukkan nilai a: ")
b = input("Masukkan nilai b: ")

# Cetak nilai variable
print("Variable a =", a)
print("Variable b =", b)

#cetak hasil operasi kedua variable dengan format string
print("Hasil penggabungan {} & {} = {}".format(a, b, a + b))

# konversi nilai variable
a = int(a)
b = int(b)
print("Hasil penjumlahan {} + {} = {}".format(a, b, a + b))
print("hasil pembagian  {} / {} = {}".format(a, b, a / b))