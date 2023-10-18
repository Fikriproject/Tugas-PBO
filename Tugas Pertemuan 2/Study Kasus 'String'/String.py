print(">>>Selamat Datang di pengecekan anggota Kelas C<<<")

# Daftar anggota kelas c
anggota_organisasi = ["Fikri", "Ilham", "Friza", "Dio", "Raihan", "Abdan", "Hafid", "Fitri", "Lubna", "Farhan", "Moh Farhan", "Putra", "Konidia", "Lulu", "Lilis", "Isro", "Lugas", "Rama", "Alif", "Wawan", "Raka"]

# String yang mau di periksa
ulang = "yes"
while ulang == "yes":
    nama = input ("Nama Anggota yang ingin di cek:")

# Bagian Pemeriksa termasuk kelas c atau bukan
    if nama not in anggota_organisasi:
        print(f"{nama} bukan anggota Kelas C.")
    else:
        print(f"{nama} adalah anggota Kelas C.")


    ulang = input ("ulang? (yes/no)").lower()
    
    