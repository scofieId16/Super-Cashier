from Transaksi import *
import datetime as dt

header = ("""
================= /////////////////////////////////// =================

=================== SELAMAT DATANG DI FAISAL MART ===================
------------------------- Selamat Berbelanja --------------------------

================= .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. =================
""")
scr = ('''
            
========================== DAFTAR BELANJA ANDA ==========================           
''')

print(header)

# Membuat objek transaksi dengan tsc
tsc = transaction()

# Customer memasukkan ID
customer_name = tsc.nama_customer
transaction_id = tsc.id_transaksi
hari_ini = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

strip = ("""
---------------------------------------------------------------------
""")
print(strip)
print(f"Selamat datang {customer_name}!")
print(f"ID transaksi   :  {transaction_id}")
print(f"Tanggal        :  {hari_ini}")

# Menampilkan menu utama
while True:
    print("\n1. Tambah produk")
    print("2. Perbarui produk")
    print("3. Perbarui jumlah produk")
    print("4. Perbarui harga produk")
    print("5. Hapus produk dari daftar belanja")
    print("6. Cek daftar belanja ")
    print("7. Reset daftar belanja")
    print("8. Pembayaran")
    print("0. Keluar\n")

    # Memasukkan pilihan menu
    try:
        choice = int(input("Masukkan pilihan Anda : "))
    except ValueError:
        print("Data yang Anda tidak sesuai")
        continue

    if choice == 1:
        tsc.add_item()

    elif choice == 2:
        tsc.update_item()

    elif choice == 3:
        tsc.update_jumlah()

    elif choice == 4:
        tsc.update_harga()

    elif choice == 5:
        tsc.delete_item()

    elif choice == 6:
        print(f"Nama Customer  :  {customer_name}")
        print(f"ID transaksi   :  {transaction_id}")
        print(f"Tanggal        :  {hari_ini}")
        print(scr)
        tsc.cek_keranjang()

    elif choice == 7:
        print(f"Nama Customer  :  {customer_name}")
        print(f"ID transaksi   :  {transaction_id}")
        print(f"Tanggal        :  {hari_ini}")
        print(scr)
        tsc.reset_transaksi()

    elif choice == 8:
        print(f"Nama Customer  :  {customer_name}")
        print(f"ID transaksi   :  {transaction_id}")
        print(f"Tanggal        :  {hari_ini}")
        print(scr)
        tsc.total_belanja()
        print("Terima kasih sudah berbelanja di FAISAL MART 😊")
        break

    elif choice == 0:
        print("Terima kasih sudah berbelanja FAISAL MART 😊")
        break

    else:
        print("Menu tidak tersedia")