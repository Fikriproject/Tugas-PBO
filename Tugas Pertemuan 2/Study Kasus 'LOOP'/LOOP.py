# input modal, harga jual dan banyak barang yang terjual
Jumlah_modal_awal = float (input ("Masukan Modal anda :"))
harga_jual = float(input("Masukan Harga jual :"))
Jumlah_Barang = int(input("masukan jumlah barang yang terjual :"))

# rumus menghitung untung dan rugi
Total_Untung = (Jumlah_modal_awal - Jumlah_modal_awal) * Jumlah_Barang
for untung in range(Jumlah_Barang):
    Total_untung = (harga_jual - Jumlah_modal_awal) * Jumlah_Barang
    
print(f"Setelah  tejual {Jumlah_Barang}, total keuntungan Anda akan menjadi: ${Total_untung:.2f}")
    