class Reamur:
    def __init__(self, suhu_reamur):
        self.suhu_reamur = suhu_reamur

    def get_Reamur(self):
        val = self.suhu_reamur
        return val

    def get_fahrenheit(self):
        val = (9/4 * self.get_Reamur()) + 32
        return val

    def get_kelvin(self):
        val = (5/4 *self.get_Reamur()) + 273
        return val
    
    def get_celcius(self):
        val = (5/4 * self.get_Reamur()) 
        return val

suhu_reamur = float(input("Masukkan suhu dalam Reamur: "))
R = Reamur(suhu_reamur)
val = R.get_Reamur()

F = R.get_fahrenheit()
C = R.get_celcius()
K = R.get_kelvin()

print(str(val) + " Reamur sama dengan:")
print(str(F) + " Fahrenheit")
print(str(C) + " Celcius")
print(str(K) + " Kelvin")
