from tkinter import Frame, Label, Entry, Button, Tk, messagebox

class PersegiPanjang:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack()

        Label(mainFrame, text='Panjang:').grid(row=0, column=0, padx=5, pady=5)
        Label(mainFrame, text='Lebar:').grid(row=1, column=0, padx=5, pady=5)
        self.txtPanjang = Entry(mainFrame)
        self.txtPanjang.grid(row=0, column=1, padx=5, pady=5)
        self.txtLebar = Entry(mainFrame)
        self.txtLebar.grid(row=1, column=1, padx=5, pady=5)

        btnHitungLuas = Button(mainFrame, text='Hitung Luas', command=self.onHitungLuas)
        btnHitungLuas.grid(row=2, column=0, padx=5, pady=5)
        
        btnHitungKeliling = Button(mainFrame, text='Hitung Keliling', command=self.onHitungKeliling)
        btnHitungKeliling.grid(row=2, column=1, padx=5, pady=5)

        self.txtHasil = Entry(mainFrame, state='readonly')
        self.txtHasil.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def onHitungLuas(self):
        try:
            panjang = float(self.txtPanjang.get())
            lebar = float(self.txtLebar.get())
            luas = panjang * lebar
            self.tampilkanHasil(luas)
        except ValueError:
            messagebox.showerror("Error", "Panjang dan Lebar harus berupa angka.")

    def onHitungKeliling(self):
        try:
            panjang = float(self.txtPanjang.get())
            lebar = float(self.txtLebar.get())
            keliling = 2 * (panjang + lebar)
            self.tampilkanHasil(keliling)
        except ValueError:
            messagebox.showerror("Error", "Panjang dan Lebar harus berupa angka.")

    def tampilkanHasil(self, hasil):
        self.txtHasil.config(state='normal')
        self.txtHasil.delete(0, 'end')
        self.txtHasil.insert(0, str(hasil))
        self.txtHasil.config(state='readonly')

if __name__ == '__main__':
    root = Tk()
    aplikasi = PersegiPanjang(root, "Program Persegi Panjang")
    root.mainloop()
