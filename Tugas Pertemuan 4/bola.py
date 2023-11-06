import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W
from math import pi

def hitung_luas():
    r = float(txtjari_jari.get())

    L = round((4 * pi * r**2),2)

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    r = float(txtjari_jari.get())

    V = round((4/3 * pi * r**3),2)

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

#create tkinter object
app = tk.Tk()

#tambahkan judul
app.title("KALKULATOR LUAS DAN VOLUME BOLA")

#windows
frame = Frame(app)
frame.pack(padx=40, pady=40)

#NAMA
nama = Label(frame, text="MUCHAMAD FIKRI ALI")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

#Label jari jari
jari_jari = Label(frame, text="jari jari:")
jari_jari.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox jari jari
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=1, column=1)

#Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

#Output label Luas
luas = Label(frame, text="Luas :")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

#Output label Volume
volume = Label(frame, text="volume :")
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

#Output Textbox Luas
txtLuas= Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

#output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()