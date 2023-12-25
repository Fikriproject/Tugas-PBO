print("Konversi Suhu Fahrenheit")

# Fungsi Konversi
def get_celcius(suhu):
    return 5/9 * (float(suhu_Fahrenheit) - 32)

def get_reamur(suhu):
    return 4/9 * (float(suhu_Fahrenheit) - 32)

def get_kelvin(suhu):
    return 5/9 * (float(suhu_Fahrenheit) - 32) + 273

# Entry
suhu_Fahrenheit = input("Masukkan suhu dalam Fahrenheit: ")

# Menggunakan Fungsi Konversi
C = get_celcius(suhu_Fahrenheit)
R = get_reamur(suhu_Fahrenheit)
K = get_kelvin(suhu_Fahrenheit)

# Output
print(suhu_Fahrenheit + " Fahrenheit sama dengan ")
print(str(C) + " Celcius")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")
