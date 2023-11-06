import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    s = float(txtsisi.get())

    L = round((6 * s**2),2)

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    s = float(txtsisi.get())

    V = round((s**3),2)

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

#create tkinter object
app = tk.Tk()

#tambahkan judul
app.title("KALKULATOR LUAS DAN VOLUME KUBUS")

#windows
frame = Frame(app)
frame.pack(padx=40, pady=40)

#NAMA
nama = Label(frame, text="MUCHAMAD FIKRI ALI")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

#Label jari jari
sisi = Label(frame, text="sisi:")
sisi.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox jari jari
txtsisi = Entry(frame)
txtsisi.grid(row=1, column=1)

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