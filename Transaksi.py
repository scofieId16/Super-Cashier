import pandas as pd
import random
import sqlite3
import datetime as dt

# Membuat class Transaction
class transaction:
    # Menginisialisasi dictionary
    def __init__(self):
        """
        Fungsi ini adalah untuk menginisiasi dictionary item yang akan diinputkan pembeli 
        dan id transaksi yang digenerate secara acak 
        serta mengatur nama database yang akan digunakan dalam prompt sqlite
        """

        self.keranjang = {}
        self.nama_customer = input("Masukkan nama Anda: ").capitalize()
        self.id_transaksi = self.generate_transaction_id() 
        self.db_name = 'C:\sqlite\db_latihandb.db'  # Nama database yang akan gunakan di prompt sqlite
        self.create_table() # Membuat tabel pada database jika belum ada
        self.counter_transaksi = 0
        self.hari_ini = dt.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    # Menggenerate ID transaksi secara acak    
    def generate_transaction_id(self):
        """
        Fungsi ini adalah untuk menghasilkan ID transaksi secara acak antara 10000000 dan 99999999
        """

        transaction_id = random.randint(10000000, 99999999)
        return transaction_id

    # Menambahkan item produk
    def add_item(self):
        """
        Fungsi ini adalah untuk menambahkan item produk ke dalam dictionary keranjang 
        yang telah kita buat sebelumnya.

        nama_item (str): Nama produk yang ingin ditambahkan.
        new_id_transaksi (int) : Id transaksi dari produk yang ditambahkan
        jumlah_item (int): Jumlah produk yang ingin ditambahkan.
        harga_item (int): Harga per pcs dari produk yang ingin ditambahkan.

        Setelah informasi dimasukkan, item akan ditambahkan ke keranjang dengan 'nama_item' sebagai key
        dan [new_id_transaksi, jumlah_item, harga_item, total_harga] sebagai value.
        """

        while True:
            try:
                nama_item = input("Masukkan nama produk: ").capitalize()
                if not nama_item:
                    print("Input is empty. Silakan masukkan nama produk.")
                    continue

                valid_jumlah = False
                while not valid_jumlah:
                    jumlah_item_str = input("Masukkan jumlah produk: ")
                    if not jumlah_item_str:
                        print("Input is empty. Silakan masukkan jumlah produk yang sesuai.")
                    else:
                        try:
                            jumlah_item = int(jumlah_item_str)
                            valid_jumlah = True
                        except ValueError:
                            print("Input tidak valid. Masukkan angka untuk jumlah produk.")

                valid_harga = False
                while not valid_harga:
                    harga_item_str = input("Masukkan harga produk: ")
                    if not harga_item_str:
                        print("Input is empty. Silakan masukkan harga produk yang sesuai.")
                    else:
                        try:
                            harga_item = int(harga_item_str)
                            valid_harga = True
                        except ValueError:
                            print("Input tidak valid. Masukkan angka untuk harga produk.")

                total_harga = jumlah_item * harga_item
                self.counter_transaksi += 1
                new_id_transaksi = f"{self.id_transaksi}_{self.counter_transaksi:02d}"
                self.keranjang.update({nama_item: [new_id_transaksi, jumlah_item, harga_item, total_harga]})
                print(f"Item {nama_item} berhasil ditambahkan")

                while True:
                    pilihan = input("Apakah Anda ingin menambahkan item lagi? (yes/no): ").lower()
                    if pilihan == 'no':
                        return "Input item selesai"
                    elif pilihan == 'yes':
                        break
                    else:
                        print("Pilihan tidak valid. Input 'yes' untuk melanjutkan atau 'no' untuk selesai.")
            except ValueError:
                print("Data yang Anda masukkan tidak sesuai")

    # Mengupdate nama produk
    def update_item(self):
        """
        Fungsi ini adalah untuk memperbarui nama produk dalam dictionary keranjang.

        nama_item (str) : Nama produk yang ingin diganti
        new_nama_item (str) : Nama produk yang baru

        Setelah informasi dimasukkan, nama produk dalam keranjang akan diperbarui dengan nama baru.
        """

        try:
            nama_item = input("Masukkan nama produk yang ingin diupdate: ").capitalize()
            if nama_item in self.keranjang:
                new_nama_item = input("Masukkan nama produk baru: ").capitalize()
                self.keranjang[new_nama_item] = self.keranjang.pop(nama_item)
                print(f"{nama_item} telah diupdate menjadi {new_nama_item}")
            else:
                print(f"{nama_item} tidak ada dalam daftar")
        except ValueError:
            print("Data yang Anda masukkan salah")

    # Mengupdate jumlah produk
    def update_jumlah(self):
        """
        Fungsi ini adalah untuk mengubah jumlah produk yang sudah ditambahkan sebelumnya

        nama_item (str) : Nama produk yang ingin diganti jumlahnya
        new_jumlah_item (int) : Jumlah produk yang baru
        """
        
        try:
            nama_item = input("Masukkan nama produk: ")
            nama_item = nama_item.capitalize()
            if nama_item in self.keranjang:
                jumlah_item = self.keranjang[nama_item][1]
                new_jumlah_item = int(input("Masukkan jumlah produk baru: "))
                self.keranjang[nama_item][1] = new_jumlah_item
                harga_item = self.keranjang[nama_item][2]
                total_harga = new_jumlah_item * harga_item
                self.counter_transaksi += 1
                new_id_transaksi = f"{self.id_transaksi}_{self.counter_transaksi:02d}"
                self.keranjang.update({nama_item: [new_id_transaksi, new_jumlah_item, harga_item, total_harga]})
                print(f"Jumlah {nama_item} telah diperbarui dari {jumlah_item} menjadi {new_jumlah_item}")
            else:
                print(f"{nama_item} tidak ada dalam daftar")
        except ValueError:
            print("Data yang Anda masukkan tidak sesuai")

    # Mengupdate harga produk
    def update_harga(self):
        
        """
        Fungsi ini adalah untuk mengubah harga produk yang sudah ditambahkan sebelumnya

        nama_item (str) : Nama produk yang ingin diganti Harganya
        new_harga_item (int) : Harga produk yang baru
        """
        
        try:
            nama_item = input("Masukkan nama produk: ")
            nama_item = nama_item.capitalize()
            if nama_item in self.keranjang:
                harga_item = self.keranjang[nama_item][2]
                new_harga_item = int(input("Masukkan harga produk baru: "))
                self.keranjang[nama_item][2] = new_harga_item
                jumlah_item = self.keranjang[nama_item][1]
                total_harga = jumlah_item * new_harga_item
                self.counter_transaksi += 1
                new_id_transaksi = f"{self.id_transaksi}_{self.counter_transaksi:02d}"
                self.keranjang.update({nama_item: [new_id_transaksi, jumlah_item, new_harga_item, total_harga]})
                print(f"Harga {nama_item} telah diperbarui dari {harga_item} menjadi {new_harga_item}")
            else:
                print(f"{nama_item} tidak ada dalam daftar")
        except ValueError:
            print("Data yang Anda masukkan tidak sesuai")

    # Menghapus daftar produk
    def delete_item(self):
        """
        Fungsi ini adalah untuk menghapus sebuah produk yang sudah ditambahkan sebelumnya,
        termasuk nama produk, jumlah dan harganya

        nama_item (str) : Nama produk yang ingin dihapus
        """
        nama_item = input("Masukkan nama produk: ").capitalize()
        if nama_item in self.keranjang:
            self.keranjang.pop(nama_item)
            print(f"{nama_item} sudah dihapus dari daftar")
        else:
            print(f"{nama_item} tidak ada dalam daftar")

    # Melakukan check transaksi
    def cek_keranjang(self):
        """
        Fungsi ini akan menampilkan keranjang dari item yang dibeli.
        """

        print("\n------------ Super Cashier -------------")
        print("------------ List Transaction  ------------\n")
        if len(self.keranjang) == 0:
            print("Anda tidak memiliki item pada keranjang")
        else:
            kolom = pd.DataFrame.from_dict(self.keranjang, orient='index', columns=['Id Transaksi', 'Jumlah', 'Harga', 'Total Harga'])
            print(kolom)

    # Mereset daftar transaksi
    def reset_transaksi(self):
        """
        Fungsi ini digunakan untuk mereset/menghapus seluruh daftar belanja yang telah ditambahkan
        """
        
        self.keranjang.clear()
        print("Daftar belanja telah dihapus")
    
    # Menghitung total belanja yang sudah dibeli
    def total_belanja(self):
        
        """
        Fungsi ini digunakan untuk menghitung total belanja, 
        diskon yang didapat dan harga setelah diskon 
        serta memasukkan pembayaran dan kembalian yang didapat
        """
        

        self.total_belanja = 0
        for value in self.keranjang.values():
            jumlah_item = value[1]
            harga_item = value[2]
            self.total_belanja += (jumlah_item * harga_item)

        dapat_diskon, diskon = self.dapat_diskon(self.total_belanja)
        self.final_price = self.total_belanja * (1 - diskon)

        if dapat_diskon == True:
            print(f'Total Belanja anda adalah Rp. {self.total_belanja:.0f}. Selamat Anda mendapat diskon sebesar {diskon * 100:.0f}%, sehingga Anda hanya perlu membayar Rp.{self.final_price:.2f}')
        else:
            print(f"Total yang harus Anda bayar adalah Rp. {self.total_belanja:.0f}")
        
        while True:
            try:
                payment = int(input("Jumlah uang Anda: Rp. "))
                if payment < self.final_price:
                    print("Jumlah uang yang Anda masukkan kurang")
                elif payment == self.final_price:
                    print("Anda membayar dengan uang pas")
                    break
                else:
                    change = payment - self.final_price
                    print(f"Uang kembalian: Rp. {change:.0f}")
                    break
            except ValueError:
                print("Data yang Anda masukkan tidak sesuai")
        
        # Setelah transaksi selesai, panggil fungsi insert_to_table
        self.insert_to_table()

    def dapat_diskon(self, total_belanja):
        """
        Fungsi ini akan memeriksa total harga belanja dan menentukan apakah pelanggan
        memenuhi syarat untuk mendapatkan diskon.

        total_belanja (float): Total harga belanja.
        dapat_diskon (bool): True jika pelanggan berhak mendapatkan diskon, False jika tidak.
        diskon (float): Persentase diskon yang diterapkan berdasarkan total belanja, 
                        akan bernilai 0.0 jika pelanggan tidak berhak mendapatkan diskon.
        """

        self.total_belanja = total_belanja
        if self.total_belanja <= 200000:
            dapat_diskon = False
            diskon = 0.0
        else:
            dapat_diskon = True
        if self.total_belanja > 500000:
            diskon = 0.1
        elif total_belanja > 300000:
            diskon = 0.08
        elif total_belanja > 200000:
            diskon = 0.05
        
        return (dapat_diskon, diskon)
    
    def insert_to_table(self):
        """
        Fungsi ini akan memasukkan detail transaksi yang ada dalam keranjang ke dalam tabel database di sqlite.
        Setiap item dalam keranjang akan dijabarkan dengan informasi seperti nama item, jumlah item, 
        harga per item, total harga sebelum dan setelah diskon (jika berlaku), 
        serta ID transaksi yang terkait.
        """
        
        try:
            nama_pelanggan = self.nama_customer
            waktu = self.hari_ini
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            for item, details in self.keranjang.items():
                nama_item = item
                new_id_transaksi = details[0]
                jumlah_item = details[1]
                harga_item = details[2]
                total_harga = details[3]
                dapat_diskon, diskon = self.dapat_diskon(self.total_belanja)
                harga_diskon = total_harga * (1 - diskon)
                diskonsql = diskon
                harga_diskonsql = harga_diskon

                # Simpan data ke dalam tabel transaksi_supercashier beserta ID transaksi
                cursor.execute('''
                    INSERT INTO transaksi_supercashier (new_id_transaksi, tanggal_transaksi, nama_pelanggan, nama_item, jumlah_item, harga, total_harga, diskon, harga_diskon)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)
                ''', (new_id_transaksi, waktu, nama_pelanggan, nama_item, jumlah_item, harga_item, total_harga, diskonsql, harga_diskonsql))

            conn.commit()
            conn.close()
            print("Data transaksi berhasil disimpan ke dalam database.")
        except sqlite3.Error as e:
            print("Terjadi kesalahan dalam menyimpan data:", e)

    def create_table(self):
        """
        Fungsi ini akan membuat tabel dengan nama 'transaksi_supercashier' dalam database sqlite
        menggunakan parameter db_name yang telah diatur sebelumnya. Tabel ini akan memiliki
        kolom-kolom yang merepresentasikan informasi transaksi seperti nomor ID, nama item, jumlah item,
        harga per item, total harga sebelum diskon, persentase diskon, dan harga setelah diskon.
        """

        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS transaksi_supercashier (
                    new_id_transaksi VARCHAR(20) PRIMARY KEY,
                    tanggal_transaksi DATETIME,
                    nama_pelanggan TEXT,
                    nama_item TEXT,
                    jumlah_item INTEGER,
                    harga INTEGER,
                    total_harga INTEGER,
                    diskon REAL,
                    harga_diskon INTEGER
                )
            ''')

            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("Terjadi kesalahan dalam membuat tabel:", e)

    
