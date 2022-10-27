print("Menghitung luas dan keliling lingkaran")
print("--------------------------------------")

# Menginput variabel
r = int(input("Masukkan panjang jari-jari lingkaran = "))

# Rumus lingkaran
phi = 3.14
luas = phi * r * r
keliling = 2 * phi * r

# Mencetak hasil
print("Luas dan keliling lingkaran dengan jari-jari {} adalah {} dan {}".format(r, luas, keliling))
