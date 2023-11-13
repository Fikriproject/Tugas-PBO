import tkinter as tk
from tkinter import messagebox
import subprocess

def simpan_jadwal():
    nama_file = str(entry_nama_file.get())
    if not nama_file.endswith('.txt'):
        nama_file += '.txt'
    try:
        with open(nama_file, "a") as file:
            data_jadwal = f"{entry_hari.get()} - {entry_mata_kuliah.get()} - {entry_Dosen.get()} - {entry_SKS.get()} - {entry_waktu.get()}\n"
            file.write(data_jadwal)
        messagebox.showinfo("Sukses", "Jadwal berhasil disimpan!")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

import subprocess

def tampilkan_jadwal():
    nama_file = str(entry_nama_file.get())
    if not nama_file.endswith('.txt'):
        nama_file += '.txt'
    try:
        subprocess.Popen([nama_file], shell=True)
    except FileNotFoundError:
        messagebox.showinfo("Info", "File jadwal tidak ditemukan.")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")


# Membuat GUI
app = tk.Tk()
app.title("Aplikasi Jadwal Kuliah")
app.geometry("350x450")


label_nama = tk.Label(app, text="Muchamad Fikri Ali")
label_nama.grid(row=1, column=0, padx=10, pady=10, sticky='e')
label_nama = tk.Label(app, text="Jadwal Perkuliahan Semester 3")
label_nama.grid(row=2, column=0, padx=10, pady=10, sticky='e')

# Label dan Entry untuk data
label_hari = tk.Label(app, text="Hari:")
label_hari.grid(row=3, column=0, padx=10, pady=10)
entry_hari = tk.Entry(app)
entry_hari.grid(row=4, column=0, padx=10, pady=10)

label_mata_kuliah = tk.Label(app, text="Mata Kuliah:")
label_mata_kuliah.grid(row=3, column=1, padx=10, pady=10)
entry_mata_kuliah = tk.Entry(app)
entry_mata_kuliah.grid(row=4, column=1, padx=10, pady=10)

label_Dosen = tk.Label(app, text="Dosen Pengampu:")
label_Dosen.grid(row=5, column=0, padx=10, pady=10)
entry_Dosen = tk.Entry(app)
entry_Dosen.grid(row=6, column=0, padx=10, pady=10)

label_SKS = tk.Label(app, text="Jumlah SKS:")
label_SKS.grid(row=5, column=1, padx=10, pady=10)
entry_SKS = tk.Entry(app)
entry_SKS.grid(row=6, column=1, padx=10, pady=10)

label_waktu = tk.Label(app, text="Waktu:")
label_waktu.grid(row=7, column=0, padx=10, pady=10)
entry_waktu = tk.Entry(app)
entry_waktu.grid(row=8, column=0, padx=10, pady=10)

label_file = tk.Label(app, text="Masukan Nama File")
label_file.grid(row=7, column=1, padx=10, pady=10)
entry_nama_file = tk.Entry(app)
entry_nama_file.grid(row=8, column=1, padx=10, pady=10)

# Tombol Simpan Jadwal
button_simpan = tk.Button(app, text="Simpan Jadwal", command=simpan_jadwal)
button_simpan.grid(row=9, column=0, pady=10)

# Tombol Tampilkan Jadwal
button_tampilkan = tk.Button(app, text="Tampilkan Jadwal", command=tampilkan_jadwal)
button_tampilkan.grid(row=9, column=1, pady=10)

# Menjalankan aplikasi
app.mainloop()