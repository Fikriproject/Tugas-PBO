# Input bilangan dari pengguna
print (">>>Selamat Datang Di aplikasi penentu bilangan Ganjil,Genap,Nol<<<")
bilangan = int(input("Masukkan sebuah bilangan bulat: "))

# Menentukan apakah bilangan ganjil, genap, atau nol
if bilangan == 0:
    print("Bilangan nol")
elif bilangan % 2 == 0:
    print("Bilangan genap")
else:
    print("Bilangan ganjil")
