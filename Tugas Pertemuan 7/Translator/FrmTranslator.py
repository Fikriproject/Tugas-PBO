from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W, ttk
from googletrans import Translator

class FrmTranslator:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("500x300")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        background_label = Label(mainFrame, text='', bg='lightblue')
        background_label.place(relwidth=1, relheight=1)
        
        Label(mainFrame, text="Pilih Bahasa :").grid(row=0, column=0, pady=5, padx=5)
        # Pasang Combobox untuk pilihan bahasa di paling atas
        self.comboboxBahasa = ttk.Combobox(mainFrame, values=['su', 'jw', 'tr'], state="readonly")
        self.comboboxBahasa.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self.comboboxBahasa.set('su')  # Pilihan default

        # Pasang Label
        Label(mainFrame, text='Masukkan teks:').grid(row=7, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Hasil Terjemahan:').grid(row=9, column=0,
            sticky=W, padx=5, pady=5)

        # Pasang Textbox
        self.txtSumber = Entry(mainFrame, width=50) 
        self.txtSumber.grid(row=7, column=1, padx=5, pady=5)

        self.txtHasil = Entry(mainFrame, width=50) 
        self.txtHasil.grid(row=9, column=1, padx=5, pady=5)
        
        Label(mainFrame, text="Muchamad Fikri Ali").grid(row=11, column=1, pady=10, padx=10)

        # Pasang Button
        self.btnTranslate = Button(mainFrame, text='Translate!', command=self.onTranslate)
        self.btnTranslate.grid(row=8, column=1, padx=5, pady=5) 

    def onTranslate(self):
        self.txtHasil.delete('0', END)
        
        penterjemah = Translator()
        bahasa_tujuan = self.comboboxBahasa.get()

        hasil = penterjemah.translate(self.txtSumber.get(), src='id', dest=bahasa_tujuan) 
        self.txtHasil.insert(END, hasil.text)
        
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmTranslator(root, "Program Translator")
    root.mainloop()
