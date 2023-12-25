print("Konversi Suhu Reamur")

# Fungsi Konversi
def get_celcius(suhu):
    return 5/4 * float(suhu)

def get_fahrenheit(suhu):
    return (9/4 * float(suhu)) + 32


def get_kelvin(suhu):
    return 5/4 * float(suhu) + 273

# Entry
suhu_reamur = input("Masukkan suhu dalam Reamur: ")

# Menggunakan Fungsi Konversi
F = get_fahrenheit(suhu_reamur)
C = get_celcius(suhu_reamur)
K = get_kelvin(suhu_reamur)

# Output
print(suhu_reamur + " Reamur sama dengan ")
print(str(C) + " Celcius")
print(str(F) + " Fahrenheit")
print(str(K) + " Kelvin")
