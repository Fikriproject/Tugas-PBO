print("Konversi Suhu Reamur")

# Fungsi Konversi
def get_celcius(suhu):
    return float(suhu) - 273

def get_fahrenheit(suhu):
    return 9/5 * (float(suhu) - 273)+ 32


def get_Reamur(suhu):
    return 4/5 * (float(suhu) - 273)

# Entry
suhu_kelvin = input("Masukkan suhu dalam Reamur: ")

# Menggunakan Fungsi Konversi
F = get_fahrenheit(suhu_kelvin)
C = get_celcius(suhu_kelvin)
R = get_Reamur(suhu_kelvin)

# Output
print(suhu_kelvin + " Kelvin sama dengan ")
print(str(C) + " Celcius")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")
