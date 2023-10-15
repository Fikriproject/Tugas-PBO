from tkinter import Frame, Label, Entry, Button, Tk, messagebox
import math

class Lingkaran:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack()

        Label(mainFrame, text='Jari-Jari:').grid(row=0, column=0, padx=5, pady=5)
        self.txtJariJari = Entry(mainFrame)
        self.txtJariJari.grid(row=0, column=1, padx=5, pady=5)

        btnHitungLuas = Button(mainFrame, text='Hitung Luas', command=self.onHitungLuas)
        btnHitungLuas.grid(row=1, column=0, padx=5, pady=5)
        
        btnHitungKeliling = Button(mainFrame, text='Hitung Keliling', command=self.onHitungKeliling)
        btnHitungKeliling.grid(row=1, column=1, padx=5, pady=5)

        self.txtHasil = Entry(mainFrame, state='readonly')
        self.txtHasil.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def onHitungLuas(self):
        try:
            jari_jari = float(self.txtJariJari.get())
            luas = math.pi * (jari_jari ** 2)
            self.tampilkanHasil(luas)
        except ValueError:
            messagebox.showerror("Error", "Jari-Jari harus berupa angka.")

    def onHitungKeliling(self):
        try:
            jari_jari = float(self.txtJariJari.get())
            keliling = 2 * math.pi * jari_jari
            self.tampilkanHasil(keliling)
        except ValueError:
            messagebox.showerror("Error", "Jari-Jari harus berupa angka.")

    def tampilkanHasil(self, hasil):
        self.txtHasil.config(state='normal')
        self.txtHasil.delete(0, 'end')
        self.txtHasil.insert(0, str(hasil))
        self.txtHasil.config(state='readonly')

if __name__ == '__main__':
    root = Tk()
    aplikasi = Lingkaran(root, "Program Lingkaran")
    root.mainloop()
