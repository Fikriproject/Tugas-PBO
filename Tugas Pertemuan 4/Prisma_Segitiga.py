import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    alas = float(txtalas.get())
    tinggi = float(txttinggi.get())
    Tp = float(txtTp.get())
    sisi1 = float(txtsisi1.get())
    sisi2 = float(txtsisi2.get())
    sisi3 = float(txtsisi3.get())

    L = round(((2*(1/2*alas*tinggi)) + ((sisi1 + sisi2 + sisi3)*Tp)),2)

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    alas = float(txtalas.get())
    tinggi = float(txttinggi.get())
    Tp = float(txtTp.get())
    sisi1 = float(txtsisi1.get())
    sisi2 = float(txtsisi2.get())
    sisi3 = float(txtsisi3.get())

    V = round(((1/2*alas*tinggi)*Tp),2)

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

#create tkinter object
app = tk.Tk()

#tambahkan judul
app.title("KALKULATOR LUAS DAN VOLUME PRISMA SEGITIGA")

#windows
frame = Frame(app)
frame.pack(padx=40, pady=40)

#NAMA
nama = Label(frame, text="MUCHAMAD FIKRI ALI")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

#Label input
alas = Label(frame, text="Alas:")
alas.grid(row=1, column=0, sticky=W, padx=5, pady=5)
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)
Tp = Label(frame, text="Tinggi Prisma:")
Tp.grid(row=3, column=0, sticky=W, padx=5, pady=5)
sisi1 = Label(frame, text="Sisi 1:")
sisi1.grid(row=4, column=0, sticky=W, padx=5, pady=5)
sisi2 = Label(frame, text="Sisi 2:")
sisi2.grid(row=5, column=0, sticky=W, padx=5, pady=5)
sisi3 = Label(frame, text="Sisi 3:")
sisi3.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Textbox input
txtalas = Entry(frame)
txtalas.grid(row=1, column=1)
txttinggi = Entry(frame)
txttinggi.grid(row=2, column=1)
txtTp = Entry(frame)
txtTp.grid(row=3, column=1)
txtsisi1 = Entry(frame)
txtsisi1.grid(row=4, column=1)
txtsisi2 = Entry(frame)
txtsisi2.grid(row=5, column=1)
txtsisi3 = Entry(frame)
txtsisi3.grid(row=6, column=1)

#Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=7, column=1, sticky=W, padx=5, pady=5)

#Output label Luas
luas = Label(frame, text="Luas :")
luas.grid(row=8, column=0, sticky=W, padx=5, pady=5)

#Output label Volume
volume = Label(frame, text="volume :")
volume.grid(row=9, column=0, sticky=W, padx=5, pady=5)

#Output Textbox Luas
txtLuas= Entry(frame)
txtLuas.grid(row=8, column=1, sticky=W, padx=5, pady=5)

#output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=9, column=1, sticky=W, padx=5, pady=5)

app.mainloop()