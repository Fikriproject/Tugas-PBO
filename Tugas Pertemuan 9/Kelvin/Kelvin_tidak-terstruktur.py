print("Konversi Suhu Kelvin")

# Entry
suhu_Kelvin = input("Masukkan suhu dalam Kelvin: ")

# Rumus
C =  float(suhu_Kelvin) - 273
F = 9/5 * (float(suhu_Kelvin) - 273)+ 32
R = 4/5 * (float(suhu_Kelvin) - 273)

# Output
print(suhu_Kelvin + " Kelvin sama dengan ")
print(str(C) + " Celcius")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")