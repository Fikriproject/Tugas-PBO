from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class FrmKelvin:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("400x300")  # Adjusted width
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10, bg="#3498db")  # Set background color to a shade of blue
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Kelvin:', font=('Helvetica', 12), bg="#3498db", fg="white").grid(row=0, column=0,sticky=W, padx=10, pady=10, columnspan=1)  
        Label(mainFrame, text="Fahrenheit:", font=('Helvetica', 12), bg="#3498db", fg="white").grid(row=2, column=0,sticky=W, padx=10, pady=10, columnspan=2)  
        Label(mainFrame, text="Celcius:", font=('Helvetica', 12), bg="#3498db", fg="white").grid(row=3, column=0,sticky=W, padx=10, pady=10, columnspan=2)  
        Label(mainFrame, text="Reamur:", font=('Helvetica', 12), bg="#3498db", fg="white").grid(row=4, column=0,sticky=W, padx=10, pady=10, columnspan=2)  

        self.txtKelvin = Entry(mainFrame, font=('Helvetica', 12))
        self.txtKelvin.grid(row=0, column=2, padx=5, pady=5, columnspan=2)

        self.txtFahrenheit = Entry(mainFrame, font=('Helvetica', 12))
        self.txtFahrenheit.grid(row=2, column=2, padx=5, pady=5, columnspan=2)

        self.txtcelcius = Entry(mainFrame, font=('Helvetica', 12))
        self.txtcelcius.grid(row=3, column=2, padx=5, pady=5, columnspan=2)

        self.txtreamur = Entry(mainFrame, font=('Helvetica', 12))
        self.txtreamur.grid(row=4, column=2, padx=5, pady=5, columnspan=2)

        self.btnHitung = Button(mainFrame, text='Hitung',
                                command=self.onHitung, bg="#2ecc71", fg="white", font=('Helvetica', 12))
        self.btnHitung.grid(row=1, column=2, padx=5, pady=5, columnspan=2)

    def get_fahrenheit(self, suhu):
        val = 9 / 5 * (suhu - 273) + 32
        return val

    def get_celcius(self, suhu):
        val = suhu - 273
        return val

    def get_reamur(self, suhu):
        val = 4 / 5 * (suhu - 273)
        return val

    def onHitung(self):
        suhu = self.txtKelvin.get()
        F = self.get_fahrenheit(float(suhu))
        self.txtFahrenheit.delete(0, END)
        self.txtFahrenheit.insert(END, str(F))

        R = self.get_celcius(float(suhu))
        self.txtcelcius.delete(0, END)
        self.txtcelcius.insert(END, str(R))

        K = self.get_reamur(float(suhu))
        self.txtreamur.delete(0, END)
        self.txtreamur.insert(END, str(K))

    def onKeluar(self, event=None):
        self.parent.destroy()


if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmKelvin(root, "Program Konversi Suhu Celcius")
    root.mainloop()
