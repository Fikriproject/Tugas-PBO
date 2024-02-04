import tkinter as tk
from tkinter import Frame, Label, Entry, Button, ttk, END, StringVar, messagebox
from tkinter.constants import NO, CENTER  # Hanya import NO dan CENTER yang diperlukan
from ttkthemes import ThemedTk
from apotek import obat

class FormObat:
    def __init__(self, root, title):
        self.root = root
        self.root.geometry("450x450")
        self.root.title(title)
        self.root.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ob = obat()
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()

    def aturKomponen(self):
        mainFrame = Frame(self.root, bd=10)
        mainFrame.pack(fill=tk.BOTH, expand=tk.YES)

        Label(mainFrame, text='kdobat:').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtkdobat = Entry(mainFrame)
        self.txtkdobat.grid(row=0, column=1, padx=5, pady=5)
        self.txtkdobat.bind("<Return>", self.onCari)

        Label(mainFrame, text='Nama:').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtNama = Entry(mainFrame)
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)

        Label(mainFrame, text='Berat:').grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtBerat = Entry(mainFrame)
        self.txtBerat.grid(row=2, column=1, padx=5, pady=5)

        Label(mainFrame, text='Bentuk:').grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtBentuk = StringVar()
        Cbo = ttk.Combobox(mainFrame, width=27, textvariable=self.txtBentuk)
        Cbo.grid(row=4, column=1, padx=5, pady=5)
        Cbo['values'] = ('tablet', 'kapsul', 'flush')
        Cbo.set('')

        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10, bg='green', fg='white')
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10, bg='blue', fg='white')
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10, bg='red', fg='white')
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        self.btnCari = Button(mainFrame, text='Cari', command=self.onCari, width=10, bg='orange', fg='white')
        self.btnCari.grid(row=3, column=3, padx=5, pady=5)

        columns = ('id', 'kdobat', 'nama', 'berat', 'bentuk')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, stretch=NO, width=80, anchor=CENTER)  # Menetapkan lebar kolom secara langsung
        self.tree.place(x=0, y=200)

    def onClear(self, event=None):
        self.txtkdobat.delete(0, END)
        self.txtNama.delete(0, END)
        self.txtBerat.delete(0, END)
        self.txtBentuk.set('')
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False

    def onReload(self):
        result = self.ob.getAllData()
        self.tree.delete(*self.tree.get_children())
        for row_data in result:
            self.tree.insert('', END, values=row_data)

    def onCari(self, event=None):
        kdobat = self.txtkdobat.get()
        res = self.ob.getBykdobat(kdobat)
        rec = self.ob.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan")
            self.ditemukan = False
            self.txtNama.focus()
        return res

    def TampilkanData(self, event=None):
        kdobat = self.txtkdobat.get()
        res = self.ob.getBykdobat(kdobat)
        self.txtNama.delete(0, END)
        self.txtNama.insert(END, self.ob.nama)
        self.txtBerat.delete(0, END)
        self.txtBerat.insert(END, self.ob.berat)
        self.txtBentuk.set(self.ob.bentuk)
        self.btnSimpan.config(text="Update")

    def onSimpan(self, event=None):
        kdobat = self.txtkdobat.get()
        nama = self.txtNama.get()
        berat = self.txtBerat.get()
        bentuk = self.txtBentuk.get()

        self.ob.kdobat = kdobat
        self.ob.nama = nama
        self.ob.berat = berat
        self.ob.bentuk = bentuk

        if self.ditemukan:
            try:
                res = self.ob.updateBykdobat(kdobat)
                ket = 'Diperbarui'
            except Exception as e:
                messagebox.showwarning("showwarning", f"Terjadi kesalahan: {str(e)}")
                return
        else:
            try:
                res = self.ob.simpan()
                ket = 'Disimpan'
            except Exception as e:
                messagebox.showwarning("showwarning", f"Terjadi kesalahan: {str(e)}")
                return

        rec = self.ob.affected
        if rec > 0:
            messagebox.showinfo("showinfo", f"Data Berhasil {ket}")
        else:
            messagebox.showwarning("showwarning", f"Data Gagal {ket}")
        self.onClear()
        return rec

    def onDelete(self, event=None):
        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data?"):
            kdobat = self.txtkdobat.get()
            self.ob.kdobat = kdobat
            if self.ditemukan:
                try:
                    res = self.ob.deleteBykdobat(kdobat)
                    rec = self.ob.affected
                except Exception as e:
                    messagebox.showwarning("showwarning", f"Terjadi kesalahan: {str(e)}")
                    return
            else:
                messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
                rec = 0

            if rec > 0:
                messagebox.showinfo("showinfo", "Data Berhasil dihapus")

            self.onClear()

    def onKeluar(self, event=None):
        self.root.destroy()

if __name__ == '__main__':
    root = ThemedTk(theme="plastik")
    aplikasi = FormObat(root, "Aplikasi Data obat")
    root.mainloop()