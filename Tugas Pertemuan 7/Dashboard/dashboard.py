import tkinter as tk
from tkinter import Menu, Label
from BangunD import KalkulatorBangunDatar
from Bangun_ruang import KalkulatorBangunRuang


def destroy_window(window):
    window.destroy()

def new_window(_class):
        new = tk.Toplevel(root)
        new.title(_class.__name__)
        _class(new)

# root window app
root = tk.Tk()
root.title('Menu Demo')
root.geometry("900x400")

# membuat menu bar
menubar = Menu(root)
root.config(menu=menubar)

# membuar menu
file_menu = Menu(menubar)
data_menu = Menu(menubar)

# menambah menu item
file_menu.add_command(
    label='File Open', command=root.destroy
)

file_menu.add_command(
    label='Exit', command=root.destroy
)

data_menu.add_command(
    label='Kalkulator Bangun Datar', command=lambda: new_window(KalkulatorBangunDatar)
)
data_menu.add_command(
    label='Kalkulator Bangun Ruang', command=lambda: new_window(KalkulatorBangunRuang)
)

# mamasukan menu ke menubar
menubar.add_cascade(
    label="File", menu=file_menu
)
menubar.add_cascade(
    label="App", menu=data_menu
)

# membuat label
label_text = "Selamat datang di Dashboard Aplikasi"
label = Label(root, text=label_text, font=("Helvetica", 16))

# memposisikan label
label.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
