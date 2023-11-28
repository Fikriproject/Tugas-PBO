import tkinter as tk
from tkinter import ttk
from math import pi

class KalkulatorBangunRuang: # class aplikasi 
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Bangun Datar")
        self.initUI()
        self.style = ttk.Style()
        self.style.theme_use("alt")
    # def UI
    def initUI(self):
        frame = ttk.Frame(self.root, padding=100)
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Selamat datang di Kalkulator Bangun Ruang!", background="pink").grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        
        self.pilih_label = ttk.Label(frame, text="Pilih bangun datar", background="Pink")
        self.pilih_label.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
        self.bangun_option_menu = ttk.Combobox(frame, values=["Kubus", "Balok", "Limas Segiempat", "Prisma Segitiga", "Limas Segitiga", "Silinder", "Bola"]) #Opsi Pilihan Bangun Datar Yang mau di hitung
        self.bangun_option_menu.grid(row=1, column=0, padx=5, pady=5)
        self.bangun_option_menu.bind("<<ComboboxSelected>>", self.on_bangun_selected)

    # Form Isi untuk menghitung Bangun datar
        self.form_frame = ttk.LabelFrame(frame, text="Isi Nilai", padding=10)
        self.form_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.entry1_label = ttk.Label(self.form_frame, text="Nilai 1:")
        self.entry1_label.grid(row=0, column=0, padx=5, pady=5)
        self.entry1 = ttk.Entry(self.form_frame)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)

        self.entry2_label = ttk.Label(self.form_frame, text="Nilai 2:")
        self.entry2_label.grid(row=1, column=0, padx=5, pady=5)
        self.entry2 = ttk.Entry(self.form_frame)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

        self.entry3_label = ttk.Label(self.form_frame, text="Nilai 3:")
        self.entry3_label.grid(row=2, column=0, padx=5, pady=5)
        self.entry3 = ttk.Entry(self.form_frame)
        self.entry3.grid(row=2, column=1, padx=5, pady=5)
        
        self.entry4_label = ttk.Label(self.form_frame, text="Nilai 4:")
        self.entry4_label.grid(row=3, column=0, padx=5, pady=5)
        self.entry4 = ttk.Entry(self.form_frame)
        self.entry4.grid(row=3, column=1, padx=5, pady=5)
        
        self.entry5_label = ttk.Label(self.form_frame, text="Nilai 5:")
        self.entry5_label.grid(row=4, column=0, padx=5, pady=5)
        self.entry5 = ttk.Entry(self.form_frame)
        self.entry5.grid(row=4, column=1, padx=5, pady=5)
        
    # button perintah mulai hitung
        self.hitung_button = ttk.Button(frame, text="Hitung", command=self.hitung)
        self.hitung_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.hasil_label = ttk.Label(frame, text="Hasil:")
        self.hasil_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5)
    
        # Pilihan untuk menghitung luas atau keliling
        self.pilihan_label = ttk.Label(frame, text="Pilih perhitungan:")
        self.pilihan_label.grid(row=5, column=0, padx=5, pady=5)
        self.pilihan_var = tk.StringVar()
        self.pilihan_var.set("Volume")
        self.pilihan_Volume = ttk.Radiobutton(frame, text="Volume", variable=self.pilihan_var, value="Volume", command=self.on_pilihan_selected)
        self.pilihan_Luas = ttk.Radiobutton(frame, text="Luas", variable=self.pilihan_var, value="Luas", command=self.on_pilihan_selected)
   
    def on_bangun_selected(self, event):
        bangun = self.bangun_option_menu.get()
        self.active_bangun = bangun  # Menandai bangun datar yang di pilih
        if bangun == "Kubus":
            self.entry1_label.config(text="Sisi:")
            self.entry2_label.config(text="")
            self.entry3_label.config(text="")
            self.entry4_label.config(text="")
            self.entry5_label.config(text="")
            self.entry2.delete(0, tk.END)
            self.entry3.delete(0, tk.END)
            self.entry4.delete(0, tk.END)
            self.entry5.delete(0, tk.END)
            self.pilihan_luas.grid_forget()
            self.pilihan_keliling.grid_forget()
            
        elif bangun == "Balok":
            self.entry1_label.config(text="Panjang:")
            self.entry2_label.config(text="Lebar:")
            self.entry3_label.config(text="Tinggi")
            self.entry4_label.config(text="")
            self.entry5_label.config(text="")
            self.entry3.delete(0, tk.END)
            self.entry4.delete(0, tk.END)
            self.entry5.delete(0, tk.END)
            self.pilihan_Volume.grid_forget()
            self.pilihan_Luas.grid_forget()
            
        elif bangun == "Limas Segiempat":
            self.entry1_label.config(text="Sisi A:")
            self.entry2_label.config(text="Sisi B:")
            self.entry3_label.config(text="Sisi C:")
            self.entry4_label.config(text="Sisi D:")
            self.entry5_label.config(text="Sisi E:")
            self.pilihan_Volume.grid(row=5, column=1, padx=5, pady=5)
            self.pilihan_Luas.grid(row=5, column=2, padx=5, pady=5)
            
        elif bangun == "Prisma Segitiga":
            self.entry1_label.config(text="Sisi A:")
            self.entry2_label.config(text="Sisi B:")
            self.entry3_label.config(text="Sisi C:")
            self.entry4_label.config(text="Sisi D:")
            self.entry5_label.config(text="Sisi E:")
            self.pilihan_Volume.grid(row=5, column=1, padx=5, pady=5)
            self.pilihan_Luas.grid(row=5, column=2, padx=5, pady=5)
            
        elif bangun == "Limas Segitiga":
            self.entry1_label.config(text="Alas:")
            self.entry2_label.config(text="Tinggi:")
            self.entry3_label.config(text="")
            self.entry4_label.config(text="")
            self.entry5_label.config(text="")
            self.entry4.delete(0, tk.END)
            self.entry5.delete(0, tk.END)
            self.pilihan_Volume.grid(row=5, column=1, padx=5, pady=5)
            self.pilihan_Luas.grid(row=5, column=2, padx=5, pady=5)
            
        elif bangun == "Silinder":
            self.entry1_label.config(text="Jari Jari :")
            self.entry2_label.config(text="Tinggi :")
            self.entry3_label.config(text="")
            self.entry4_label.config(text="")
            self.entry5_label.config(text="")
            self.entry4.delete(0, tk.END)
            self.entry5.delete(0, tk.END)
            self.pilihan_Volume.grid(row=5, column=1, padx=5, pady=5)
            self.pilihan_Luas.grid(row=5, column=2, padx=5, pady=5)
            
        elif bangun == "Bola":
            self.entry1_label.config(text="Jari Jari")
            self.entry2_label.config(text="")
            self.entry3_label.config(text="")
            self.entry4_label.config(text="")
            self.entry5_label.config(text="")
            self.entry4.delete(0, tk.END)
            self.entry5.delete(0, tk.END)
            self.pilihan_Volume.grid(row=5, column=1, padx=5, pady=5)
            self.pilihan_Luas.grid(row=5, column=2, padx=5, pady=5)  
            
    # membuat pilihan menghitung luas atau keliling
    def on_pilihan_selected(self):
        pilihan = self.pilihan_var.get()
        
        if self.active_bangun == "Limas Segiempat":
            if pilihan == "Volume":
                self.entry1_label.config(text="Luas Alas :")
                self.entry2_label.config(text="Tinggi :")
                self.entry3_label.config(text="")
                self.entry4_label.config(text="")
                self.entry5_label.config(text="")
            elif pilihan == "Luas":
                self.entry1_label.config(text="Luas Sisi A :")
                self.entry2_label.config(text="Luas Sisi B :")
                self.entry3_label.config(text="Luas Sisi C :")
                self.entry4_label.config(text="Luas Sisi D :")
                self.entry5_label.config(text="Luas Sisi E :")
        
        if self.active_bangun == "Prisma Segitiga":
            if pilihan == "Volume":
                self.entry1_label.config(text="Luas :")
                self.entry2_label.config(text="Tinggi :")
                self.entry3_label.config(text="")
                self.entry4_label.config(text="")
                self.entry5_label.config(text="")
            elif pilihan == "Luas":
                self.entry1_label.config(text="Luas Sisi A :")
                self.entry2_label.config(text="Luas Sisi B :")
                self.entry3_label.config(text="Luas Sisi C :")
                self.entry4_label.config(text="Tinggi :")
                self.entry5_label.config(text="Luas :")
                
        elif self.active_bangun == "Limas Segitiga":
            if pilihan == "Volume":
                self.entry1_label.config(text="Luas :")
                self.entry2_label.config(text="Tinggi :")
                self.entry3_label.config(text="")
                self.entry4_label.config(text="")
            elif pilihan == "Luas":
                self.entry1_label.config(text="Sisi A:")
                self.entry2_label.config(text="Sisi B:")
                self.entry3_label.config(text="Sisi C")
                self.entry4_label.config(text="Sisi D")
                
        elif self.active_bangun =="Silinder":
            if pilihan == "Volume":
                self.entry1_label.config(text="Jari Jari :")
                self.entry2_label.config(text="Tinggi :")
                self.entry3_label.config(text="")
                self.entry4_label.config(text="")
            elif pilihan == "Luas":
                self.entry1_label.config(text="Jari Jari :")
                self.entry2_label.config(text="Tinggi :")
                self.entry3_label.config(text="")
                self.entry4_label.config(text="")
                
        elif self.active_bangun =="Bola":
            if pilihan == "Volume":
                self.entry1_label.config(text="Jari Jari")
                self.entry2_label.config(text="")
                self.entry3_label.config(text="")
                self.entry4_label.config(text="")
            elif pilihan == "Luas":
                self.entry1_label.config(text="Jari Jari:")
                self.entry2_label.config(text="")
                self.entry3_label.config(text="")
                self.entry4_label.config(text="")
                
      # Rumus Rumus Bangun Datar      
    def hitung(self):
        bangun = self.bangun_option_menu.get()
        nilai1 = float(self.entry1.get())
        nilai2 = float(self.entry2.get()) if self.entry2.get() else 0
        nilai3 = float(self.entry3.get()) if self.entry3.get() else 0
        nilai4 = float(self.entry4.get()) if self.entry4.get() else 0
        nilai5 = float(self.entry5.get()) if self.entry5.get() else 0
        hasil = self.hitung_bangun(bangun, nilai1, nilai2, nilai3, nilai4, nilai5)
        self.hasil_label.config(text=hasil)

    def hitung_bangun(self, bangun, nilai1, nilai2, nilai3, nilai4, nilai5):
        hasil = ""
        if bangun == "Kubus":
            Volume = nilai1 ** 3
            Luas = 6 * (nilai1 ** 2)
            hasil = f"Volume: {Volume:.2f}, Luas: {Luas:.2f}"
            
        elif bangun == "Balok":
            Volume = nilai1 * nilai2 * nilai3
            Luas = 2 * ((nilai1 * nilai2) + (nilai2*nilai3) + (nilai1 * nilai3))
            hasil = f"Volume: {Volume:.2f}, Luas: {Luas:.2f}"
            
            
        elif bangun == "Limas Segiempat":
            Volume =  (nilai1 * nilai2) /3
            keliling = nilai1 + nilai2 + nilai3 + nilai4 + nilai5
            hasil = f"Volume: {Volume:.2f}, Keliling: {keliling:.2f}"
            
        elif bangun == "Prisma Segitiga":
            if self.pilihan_var.get() == "Volume":
                Volume = (nilai1 * nilai2) / 2
                hasil = f"Volume: {Volume:.2f}"
            else:
                Luas = (nilai1 + nilai2 + nilai3) * (nilai4 + nilai5)
                hasil = f"Luas: {Luas:.2f}"
                
        elif bangun == "Limas Segitiga":
            if self.pilihan_var.get() == "Volume":
                Volume = (nilai1 * nilai2) / 6
                hasil = f"Volume: {Volume:.2f}"
            else:
                Luas = nilai1 + nilai2 + nilai3 + nilai4
                hasil = f"Luas: {Luas:.2f}"
                
        elif bangun == "Silinder":
            if self.pilihan_var.get() == "Volume":
                Volume = pi * (nilai1 ** 2) * nilai2
                hasil = f"Volume: {Volume:.2f}"
            else:
                Luas = (2*pi*nilai1*nilai2) + (2*pi*(nilai1**2)*nilai2)
                hasil = f"Luas: {Luas:.2f}"
            
        elif bangun == "Bola":
            if self.pilihan_var.get() == "Volume":
                Volume =  (4/3)*pi*(nilai1**3)
                hasil = f"Volume: {Volume:.2f}"
            else :
                Luas = (4/3)*pi*(nilai1**2)
                hasil = f"Luas: {Luas:.2f}"
        
        return hasil
        
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = KalkulatorBangunRuang(root)
    root.mainloop()
