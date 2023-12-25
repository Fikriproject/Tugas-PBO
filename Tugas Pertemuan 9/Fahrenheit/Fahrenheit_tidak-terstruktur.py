print("Konversi Suhu Fahrenheit")

# Entry
suhu_Fahrenheit = input("Masukkan suhu dalam Fahrenheit: ")

# Rumus
C = 5/9 * (float(suhu_Fahrenheit) - 32)
R = 4/9 * (float(suhu_Fahrenheit) - 32)
K = 5/9 * (float(suhu_Fahrenheit) - 32) + 273

# Output
print(suhu_Fahrenheit + " Fahrenheit sama dengan ")
print(str(C) + " Celcius")
print(str(R) + " Fahrenheit")
print(str(K) + " Kelvin")