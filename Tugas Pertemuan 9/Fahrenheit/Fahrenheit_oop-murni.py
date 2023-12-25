from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class FrmFahrenheit:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("400x300")  # Adjusted width
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10, bg="sky blue")  # Set background color to sky blue
        mainFrame.pack(fill=BOTH, expand=YES)
        
        Label(mainFrame, text='Fahrenheit:', font=('Helvetica', 12), bg="skyblue").grid(row=0, column=0,sticky=W, padx=10, pady=10, columnspan=1)  # Adjusted font size and columnspan
        Label(mainFrame, text="Reamur:", font=('Helvetica', 12), bg="skyblue").grid(row=2, column=0,sticky=W, padx=10, pady=10, columnspan=2)  # Adjusted font size and columnspan
        Label(mainFrame, text="Celcius:", font=('Helvetica', 12), bg="skyblue").grid(row=3, column=0,sticky=W, padx=10, pady=10, columnspan=2)  # Adjusted font size and columnspan
        Label(mainFrame, text="Kelvin:", font=('Helvetica', 12), bg="skyblue").grid(row=4, column=0,sticky=W, padx=10, pady=10, columnspan=2)  # Adjusted font size and columnspan

        self.txtFahrenheit = Entry(mainFrame, font=('Helvetica', 12))  # Adjusted font size
        self.txtFahrenheit.grid(row=0, column=2, padx=10, pady=10, columnspan=2)  # Adjusted columnspan

        self.txtReamur = Entry(mainFrame, font=('Helvetica', 12))  # Adjusted font size
        self.txtReamur.grid(row=2, column=2, padx=10, pady=10, columnspan=2)  # Adjusted columnspan

        self.txtcelcius = Entry(mainFrame, font=('Helvetica', 12))  # Adjusted font size
        self.txtcelcius.grid(row=3, column=2, padx=10, pady=10, columnspan=2)  # Adjusted columnspan

        self.txtKelvin = Entry(mainFrame, font=('Helvetica', 12))  # Adjusted font size
        self.txtKelvin.grid(row=4, column=2, padx=10, pady=10, columnspan=2)  # Adjusted columnspan

        self.btnHitung = Button(mainFrame, text='Hitung',
                                command=self.onHitung, bg="#1877f2", fg="white", font=('Helvetica', 12))  # Adjusted font size
        self.btnHitung.grid(row=1, column=2, padx=10, pady=10, columnspan=2)  # Adjusted columnspan

    def get_Reamur(self, suhu):
        val = 4 / 9 * (float(suhu) - 32)
        return val

    def get_celcius(self, suhu):
        val = 5 / 9 * (float(suhu) - 32)
        return val

    def get_kelvin(self, suhu):
        val = 5 / 9 * (float(suhu) - 32) + 273
        return val

    def onHitung(self):
        # Suhu dalam Reamur
        suhu = self.txtFahrenheit.get()

        F = self.get_Reamur(float(suhu))
        self.txtReamur.delete(0, END)
        self.txtReamur.insert(END, str(F))

        # Suhu dalam Reamur
        R = self.get_celcius(float(suhu))
        self.txtcelcius.delete(0, END)
        self.txtcelcius.insert(END, str(R))

        # Suhu dalam Kelvin
        K = self.get_kelvin(float(suhu))
        self.txtKelvin.delete(0, END)
        self.txtKelvin.insert(END, str(K))

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()


if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmFahrenheit(root, "Program Konversi Suhu Celcius")
    root.mainloop()
