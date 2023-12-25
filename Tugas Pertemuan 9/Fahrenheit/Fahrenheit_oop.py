class Fahrenheit:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_Fahrenheit(self):
        val = self.suhu
        return val

    def get_Reamur(self):
        val = 4/9 * (self.get_Fahrenheit() - 32)
        return val

    def get_kelvin(self):
        val = 4/9 * (self.get_Fahrenheit() - 32) + 273
        return val
    
    def get_celcius(self):
        val = 5/9 * (self.get_Fahrenheit() - 32) 
        return val

suhu = float(input("Masukkan suhu dalam Fahrenheit: "))
R = Fahrenheit(suhu)
val = R.get_Fahrenheit()

R = R.get_Reamur()
C = R.get_celcius()
K = R.get_kelvin()

print(str(val) + " Reamur sama dengan:")
print(str(R) + " Reamur")
print(str(C) + " Celcius")
print(str(K) + " Kelvin")
