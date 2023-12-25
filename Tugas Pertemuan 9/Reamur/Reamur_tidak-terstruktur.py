print("Konversi Suhu Reamur")

# Entry
suhu_reamur = input("Masukkan suhu dalam Reamur: ")

# Rumus
C = 5/4 * float(suhu_reamur)
F = (9/4 * float(suhu_reamur)) + 32
K = (5/4 * float(suhu_reamur)) + 273

# Output
print(suhu_reamur + " Reamur sama dengan ")
print(str(C) + " Celcius")
print(str(F) + " Fahrenheit")
print(str(K) + " Kelvin")