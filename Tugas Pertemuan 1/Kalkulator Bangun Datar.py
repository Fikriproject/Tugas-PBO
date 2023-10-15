import tkinter as tk
from tkinter import ttk

class KalkulatorBangunDatar: # class aplikasi 
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Bangun Datar")
        self.initUI()

    # def UI
    def initUI(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Selamat datang di Kalkulator Bangun Datar!").grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.bangun_option_menu = ttk.Combobox(frame, values=["Persegi", "Persegi Panjang", "Lingkaran", "Segitiga", "Jajar Genjang", "Layang-Layang", "Belah Ketupat", "Trapesium"]) #Opsi Pilihan Bangun Datar Yang mau di hitung
        self.bangun_option_menu.grid(row=1, column=1, padx=5, pady=5)
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
        
    # button perintah mulai hitung
        self.hitung_button = ttk.Button(frame, text="Hitung", command=self.hitung)
        self.hitung_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.hasil_label = ttk.Label(frame, text="")
        self.hasil_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        # Pilihan untuk menghitung luas atau keliling
        self.pilihan_label = ttk.Label(frame, text="Pilih perhitungan:")
        self.pilihan_label.grid(row=5, column=0, padx=5, pady=5)
        self.pilihan_var = tk.StringVar()
        self.pilihan_var.set("Luas")
        self.pilihan_luas = ttk.Radiobutton(frame, text="Luas", variable=self.pilihan_var, value="Luas", command=self.on_pilihan_selected)
        self.pilihan_keliling = ttk.Radiobutton(frame, text="Keliling", variable=self.pilihan_var, value="Keliling", command=self.on_pilihan_selected)

    def on_bangun_selected(self, event):
        bangun = self.bangun_option_menu.get()
        self.active_bangun = bangun  # Menandai bangun datar yang di pilih
        if bangun == "Persegi":
            self.entry1_label.config(text="Sisi:")
            self.entry2_label.config(text="")
            self.entry3_label.config(text="")
            self.entry4_label.config(text="")
            self.entry2.delete(0, tk.END)
            self.entry3.delete(0, tk.END)
            self.entry4.delete(0, tk.END)
            self.pilihan_luas.grid_forget()
            self.pilihan_keliling.grid_forget()
            
        elif bangun == "Persegi Panjang":
            self.entry1_label.config(text="Panjang:")
            self.entry2_label.config(text="Lebar:")
            self.entry3_label.config(text="")
            self.entry4_label.config(text="")
            self.entry3.delete(0, tk.END)
            self.entry4.delete(0, tk.END)
            self.pilihan_luas.grid_forget()
            self.pilihan_keliling.grid_forget()
            
        elif bangun == "Lingkaran":
            self.entry1_label.config(text="Jari-Jari:")
            self.entry2_label.config(text="")
            self.entry3_label.config(text="")
            self.entry4_label.config(text="")
            self.entry2.delete(0, tk.END)
            self.entry3.delete(0, tk.END)
            self.entry4.delete(0, tk.END)
            self.pilihan_luas.grid_forget()
            self.pilihan_keliling.grid_forget()
            
        elif bangun == "Segitiga":
            self.entry1_label.config(text="Sisi A:")
            self.entry2_label.config(text="Sisi B:")
            self.entry3_label.config(text="Sisi C:")
            self.entry4_label.config(text="")
            self.entry4.delete(0, tk.END)
            self.pilihan_luas.grid(row=5, column=1, padx=5, pady=5)
            self.pilihan_keliling.grid(row=5, column=2, padx=5, pady=5)
            
        elif bangun == "Jajar Genjang":
            self.entry1_label.config(text="Alas:")
            self.entry2_label.config(text="Tinggi:")
            self.entry3_label.config(text="")
            self.entry4_label.config(text="")
            self.entry4.delete(0, tk.END)
            self.pilihan_luas.grid(row=5, column=1, padx=5, pady=5)
            self.pilihan_keliling.grid(row=5, column=2, padx=5, pady=5)
            
        elif bangun == "Layang-Layang":
            self.entry1_label.config(text="Diagonal 1:")
            self.entry2_label.config(text="Diagonal 2:")
            self.entry3_label.config(text="")
            self.entry4_label.config(text="")
            self.entry4.delete(0, tk.END)
            self.pilihan_luas.grid(row=5, column=1, padx=5, pady=5)
            self.pilihan_keliling.grid(row=5, column=2, padx=5, pady=5)
            
        elif bangun == "Belah Ketupat":
            self.entry1_label.config(text="Diagonal 1:")
            self.entry2_label.config(text="Diagonal 2:")
            self.entry3_label.config(text="")
            self.entry4_label.config(text="")
            self.entry4.delete(0, tk.END)
            self.pilihan_luas.grid(row=5, column=1, padx=5, pady=5)
            self.pilihan_keliling.grid(row=5, column=2, padx=5, pady=5)  
            
        elif bangun == "Trapesium":
            self.entry1_label.config(text="Sisi Atas:")
            self.entry2_label.config(text="Sisi Bawah:")
            self.entry3_label.config(text="Sisi Miring 1")
            self.entry4_label.config(text="Sisi Miring 2")
            self.pilihan_luas.grid(row=5, column=1, padx=5, pady=5)
            self.pilihan_keliling.grid(row=5, column=2, padx=5, pady=5)
            
    # membuat pilihan menghitung luas atau keliling
    def on_pilihan_selected(self):
        pilihan = self.pilihan_var.get()
        
        if self.active_bangun == "Segitiga":
            if pilihan == "Luas":
                self.entry1_label.config(text="Alas:")
                self.entry2_label.config(text="Tinggi:")
                self.entry3_label.config(text="")
                self.entry4_label.config(text="")
            elif pilihan == "Keliling":
                self.entry1_label.config(text="Sisi A:")
                self.entry2_label.config(text="Sisi B:")
                self.entry3_label.config(text="Sisi C:")
                self.entry4_label.config(text="")
                
        elif self.active_bangun == "Jajar Genjang":
            if pilihan == "Luas":
                self.entry1_label.config(text="Alas:")
                self.entry2_label.config(text="Tinggi:")
                self.entry3_label.config(text="")
                self.entry4_label.config(text="")
            elif pilihan == "Keliling":
                self.entry1_label.config(text="Sisi A:")
                self.entry2_label.config(text="Sisi B:")
                self.entry3_label.config(text="")
                self.entry4_label.config(text="")
                
        elif self.active_bangun =="Layang-Layang":
            if pilihan == "Luas":
                self.entry1_label.config(text="Diagonal 1:")
                self.entry2_label.config(text="Diagonal 2:")
                self.entry3_label.config(text="")
                self.entry4_label.config(text="")
            elif pilihan == "Keliling":
                self.entry1_label.config(text="Sisi:")
                self.entry2_label.config(text="")
                self.entry3_label.config(text="")
                self.entry4_label.config(text="")
                
        elif self.active_bangun =="Belah Ketupat":
            if pilihan == "Luas":
                self.entry1_label.config(text="Diagonal 1:")
                self.entry2_label.config(text="Diagonal 2:")
                self.entry3_label.config(text="")
                self.entry4_label.config(text="")
            elif pilihan == "Keliling":
                self.entry1_label.config(text="Sisi:")
                self.entry2_label.config(text="")
                self.entry3_label.config(text="")
                self.entry4_label.config(text="")
                
        elif self.active_bangun =="Trapesium":
            if pilihan == "Luas":
                self.entry1_label.config(text="Sisi Atas:")
                self.entry2_label.config(text="Sisi Bawah:")
                self.entry3_label.config(text="Tinggi:")
                self.entry4_label.config(text="")
            elif pilihan == "Keliling":
                self.entry1_label.config(text="Sisi Atas:")
                self.entry2_label.config(text="Sisi Bawah:")
                self.entry3_label.config(text="Sisi Miring 1")
                self.entry4_label.config(text="Sisi Miring 2")
                
      # Rumus Rumus Bangun Datar      
    def hitung(self):
        bangun = self.bangun_option_menu.get()
        nilai1 = float(self.entry1.get())
        nilai2 = float(self.entry2.get()) if self.entry2.get() else 0
        nilai3 = float(self.entry3.get()) if self.entry3.get() else 0
        nilai4 = float(self.entry4.get()) if self.entry4.get() else 0
        hasil = self.hitung_bangun(bangun, nilai1, nilai2, nilai3, nilai4)
        self.hasil_label.config(text=hasil)

    def hitung_bangun(self, bangun, nilai1, nilai2, nilai3, nilai4):
        hasil = ""
        if bangun == "Persegi":
            luas = nilai1 * nilai1
            keliling = 4 * nilai1
            hasil = f"Luas: {luas:.2f}, Keliling: {keliling:.2f}"
        elif bangun == "Persegi Panjang":
            luas = nilai1 * nilai2
            keliling = 2 * (nilai1 + nilai2)
            hasil = f"Luas: {luas:.2f}, Keliling: {keliling:.2f}"
        elif bangun == "Lingkaran":
            luas = 3.14 * nilai1 * nilai1
            keliling = 2 * 3.14 * nilai1
            hasil = f"Luas: {luas:.2f}, Keliling: {keliling:.2f}"
        elif bangun == "Segitiga":
            if self.pilihan_var.get() == "Luas":
                s = (nilai1 + nilai2 + nilai3) / 2
                luas = (s * (s - nilai1) * (s - nilai2) * (s - nilai3)) ** 0.5
                hasil = f"Luas: {luas:.2f}"
            else:
                keliling = nilai1 + nilai2 + nilai3
                hasil = f"Keliling: {keliling:.2f}"
        elif bangun == "Jajar Genjang":
            if self.pilihan_var.get() == "Luas":
                luas = nilai1 * nilai2
                hasil = f"Luas: {luas:.2f}"
            else:
                keliling = 2 * (nilai1 + nilai2)
                hasil = f"Keliling: {keliling:.2f}"
        elif bangun == "Layang-Layang":
            luas = 0.5 * nilai1 * nilai2
            d1 = nilai1
            d2 = nilai2
            keliling = 2 * (d1 + d2)
            hasil = f"Luas: {luas:.2f}, Keliling: {keliling:.2f}"
        elif bangun == "Belah Ketupat":
            luas = 0.5 * nilai1 * nilai2
            d1 = nilai1
            keliling = 4 * d1
            hasil = f"Luas: {luas:.2f}, Keliling: {keliling:.2f}"
        elif bangun == "Trapesium":
            if self.pilihan_var.get() == "Luas":
                luas = 0.5 * (nilai1 + nilai2) * nilai3
                hasil = f"Luas: {luas:.2f}"
            else:
                keliling = nilai1 + nilai2 + nilai3 + nilai4
                hasil = f"Keliling: {keliling:.2f}"
        return hasil

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = KalkulatorBangunDatar(root)
    root.mainloop()
