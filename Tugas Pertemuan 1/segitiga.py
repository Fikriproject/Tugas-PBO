from tkinter import Frame, Label, Entry, Button, Tk, messagebox
import math

class Segitiga:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack()
    
        Label(mainFrame, text='Alas:').grid(row=0, column=0, padx=5, pady=5)
        Label(mainFrame, text='Tinggi:').grid(row=1, column=0, padx=5, pady=5)
        Label(mainFrame, text='Sisi A:').grid(row=2, column=0, padx=5, pady=5)
        Label(mainFrame, text='Sisi B:').grid(row=3, column=0, padx=5, pady=5)
        Label(mainFrame, text='Sisi C:').grid(row=4, column=0, padx=5, pady=5)

        self.txtAlas = Entry(mainFrame)
        self.txtAlas.grid(row=0, column=1, padx=5, pady=5)
        self.txtTinggi = Entry(mainFrame)
        self.txtTinggi.grid(row=1, column=1, padx=5, pady=5)
        self.txtSisiA = Entry(mainFrame)
        self.txtSisiA.grid(row=2, column=1, padx=5, pady=5)
        self.txtSisiB = Entry(mainFrame)
        self.txtSisiB.grid(row=3, column=1, padx=5, pady=5)
        self.txtSisiC = Entry(mainFrame)
        self.txtSisiC.grid(row=4, column=1, padx=5, pady=5)

        btnHitungLuas = Button(mainFrame, text='Hitung Luas', command=self.onHitungLuas)
        btnHitungLuas.grid(row=5, column=0, padx=5, pady=5)
        
        btnHitungKeliling = Button(mainFrame, text='Hitung Keliling', command=self.onHitungKeliling)
        btnHitungKeliling.grid(row=5, column=1, padx=5, pady=5)

        self.txtHasil = Entry(mainFrame, state='readonly')
        self.txtHasil.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def onHitungLuas(self):
        try:
            alas = float(self.txtAlas.get())
            tinggi = float(self.txtTinggi.get())
            luas = 0.5 * alas * tinggi
            self.tampilkanHasil(luas)
        except ValueError:
            messagebox.showerror("Error", "Alas dan Tinggi harus berupa angka.")

    def onHitungKeliling(self):
        try:
            sisi_a = float(self.txtSisiA.get())
            sisi_b = float(self.txtSisiB.get())
            sisi_c = float(self.txtSisiC.get())
            keliling = sisi_a + sisi_b + sisi_c
            self.tampilkanHasil(keliling)
        except ValueError:
            messagebox.showerror("Error", "Sisi A, Sisi B, dan Sisi C harus berupa angka.")

    def tampilkanHasil(self, hasil):
        self.txtHasil.config(state='normal')
        self.txtHasil.delete(0, 'end')
        self.txtHasil.insert(0, str(hasil))
        self.txtHasil.config(state='readonly')

if __name__ == '__main__':
    root = Tk()
    aplikasi = Segitiga(root, "Program Segitiga")
    root.mainloop()
