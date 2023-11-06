import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    alas = float(txtalas.get())
    tinggi = float(txttinggi.get())

    L = round(((1/2*alas*tinggi) + (1/2*alas*tinggi) + (1/2*alas*tinggi) + (1/2*alas*tinggi) + (alas*4)),2)

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    alas = float(txtalas.get())
    tinggi = float(txttinggi.get())

    V = round(((1/3*(alas*4))*tinggi),2)

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

#create tkinter object
app = tk.Tk()

#tambahkan judul
app.title("KALKULATOR LUAS DAN VOLUME LIMAS SEGIEMPAT")

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

# Textbox input
txtalas = Entry(frame)
txtalas.grid(row=1, column=1)
txttinggi = Entry(frame)
txttinggi.grid(row=2, column=1)

#Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

#Output label Luas
luas = Label(frame, text="Luas :")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

#Output label Volume
volume = Label(frame, text="volume :")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

#Output Textbox Luas
txtLuas= Entry(frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

#output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()