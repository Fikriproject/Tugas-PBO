from tkinter import Frame, Label, Entry, Button, Tk, messagebox

class Trapesium:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack()

        Label(mainFrame, text='Sisi Atas:').grid(row=0, column=0, padx=5, pady=5)
        Label(mainFrame, text='Sisi Bawah:').grid(row=1, column=0, padx=5, pady=5)
        Label(mainFrame, text='Tinggi:').grid(row=2, column=0, padx=5, pady=5)
        Label(mainFrame, text='Sisi Miring 1:').grid(row=3, column=0, padx=5, pady=5)
        Label(mainFrame, text='Sisi Miring 2:').grid(row=4, column=0, padx=5, pady=5)

        self.txtSisiAtas = Entry(mainFrame)
        self.txtSisiAtas.grid(row=0, column=1, padx=5, pady=5)
        self.txtSisiBawah = Entry(mainFrame)
        self.txtSisiBawah.grid(row=1, column=1, padx=5, pady=5)
        self.txtTinggi = Entry(mainFrame)
        self.txtTinggi.grid(row=2, column=1, padx=5, pady=5)
        self.txtSisiMiring1 = Entry(mainFrame)
        self.txtSisiMiring1.grid(row=3, column=1, padx=5, pady=5)
        self.txtSisiMiring2 = Entry(mainFrame)
        self.txtSisiMiring2.grid(row=4, column=1, padx=5, pady=5)

        btnHitungLuas = Button(mainFrame, text='Hitung Luas', command=self.onHitungLuas)
        btnHitungLuas.grid(row=5, column=0, padx=5, pady=5)
        
        btnHitungKeliling = Button(mainFrame, text='Hitung Keliling', command=self.onHitungKeliling)
        btnHitungKeliling.grid(row=5, column=1, padx=5, pady=5)

        self.txtHasil = Entry(mainFrame, state='readonly')
        self.txtHasil.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def onHitungLuas(self):
        try:
            sisi_atas = float(self.txtSisiAtas.get())
            sisi_bawah = float(self.txtSisiBawah.get())
            tinggi = float(self.txtTinggi.get())
            luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
            self.tampilkanHasil(luas)
        except ValueError:
            messagebox.showerror("Error", "Sisi Atas, Sisi Bawah, dan Tinggi harus berupa angka.")

    def onHitungKeliling(self):
        try:
            sisi_atas = float(self.txtSisiAtas.get())
            sisi_bawah = float(self.txtSisiBawah.get())
            sisi_miring1 = float(self.txtSisiMiring1.get())
            sisi_miring2 = float(self.txtSisiMiring2.get())
            keliling = sisi_atas + sisi_bawah + sisi_miring1 + sisi_miring2
            self.tampilkanHasil(keliling)
        except ValueError:
            messagebox.showerror("Error", "Semua sisi harus berupa angka.")

    def tampilkanHasil(self, hasil):
        self.txtHasil.config(state='normal')
        self.txtHasil.delete(0, 'end')
        self.txtHasil.insert(0, str(hasil))
        self.txtHasil.config(state='readonly')

if __name__ == '__main__':
    root = Tk()
    aplikasi = Trapesium(root, "Program Trapesium")
    root.mainloop()
