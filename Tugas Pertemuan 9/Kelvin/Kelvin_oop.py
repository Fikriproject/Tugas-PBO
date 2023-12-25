class Kelvin:
    def __init__(self, suhu_Kelvin):
        self.suhu_Kelvin = suhu_Kelvin

    def get_Kelvin(self):
        val = self.suhu_Kelvin
        return val

    def get_fahrenheit(self):
        val = 9/5 * (self.get_Kelvin() - 273) + 32
        return val

    def get_Reamur(self):
        val = 4/5 * (self.get_Kelvin() - 273)
        return val
    
    def get_celcius(self):
        val = self.get_Kelvin() - 273
        return val

suhu_Kelvin = float(input("Masukkan suhu dalam Kelvin: "))
R = Kelvin(suhu_Kelvin)
val = R.get_Kelvin()

F = R.get_fahrenheit()
C = R.get_celcius()
R = R.get_Reamur()

print(str(val) + " Reamur sama dengan:")
print(str(F) + " Fahrenheit")
print(str(C) + " Celcius")
print(str(R) + " Reamur")
