# **Super Cashier Program**

### **Ahmad Faisal Fahmi, Software dan Data Engineering Batch 3**

## 1. **Latar Belakang Masalah**

Seorang pemilik salah satu supermarket besar di salah satu kota di Indonesia ingin melakukan inovasi dengan membuat sistem kasir yang dapat self-service di supermarket miliknya. Kasir self-service diharapkan mampu mempermudah customer yang datang agar bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur lainnya. Pemilik tersebut membutuhkan programmer untuk membuatkan fitur-fitur tersebut agar bisa menerapkan sistem self-service di supermarket miliknya.

## 2. **Objective & Requirement**

### Objective
Tujuan yang ingin dicapai dari project ini adalah membuat sistem kasir berbasis self-service pada supermarket untuk mempermudah Customer dalam melakukan proses transaksi belanja secara mandiri melalui aplikasi yang telah disediakan.
### Requirements
Untuk bisa mencapai tujuan tersebut, terdapat beberapa requirements yang harus terdapat pada sistem kasir self-service diantaranya:
1. Melakukan Input Nama Customer
2. Mencetak ID transaksi Customer.
3. Melakukan input nama produk, jumlah produk, dan harga produk.
4. Melakukan update nama, jumlah, atau harga item apabila terjadi kesalahan saat memasukkan input data.
5. Melakukan pembatalan/reset transaksi belanja 
6. Melakukan pengecekan terhadap daftar belanja.
7. Menampilkan total belanja, diskon yang didapat dan nominal yang perlu dibayarkan

## 3. **Flowchart**
Bagian ini menjelaskan mengenai diagram alur untuk membuat sistem kasir self service atau dikenal dengan **Super Cashier**.
Flowchart terdiri dari beberapa sub-flowchart yaitu menu utama, tambah barang, perbarui nama barang, perbarui harga barang, perbarui jumlah barang, hapus barang, hapus semua barang di keranjang, tampilkan keranjang, dan total belanja

### Flowchart Main Menu 
![Main Menu Flowchart](https://github.com/scofieId16/Super-Cashier/blob/a1661d9ecfb1e4acb65d0cab55eaf77fe7883a63/Flowchart/Mainmenu.png)

### Flowchart Add Item
![Add Item Flowchart](https://github.com/scofieId16/Super-Cashier/blob/a1661d9ecfb1e4acb65d0cab55eaf77fe7883a63/Flowchart/Additem.png)

### Flowchart Update Nama Item
![Update Item Name Flowchart](https://github.com/scofieId16/Super-Cashier/blob/a1661d9ecfb1e4acb65d0cab55eaf77fe7883a63/Flowchart/Updateitem.png)

### Flowchart Update Harga Item
![Update Item Price Flowchart](https://github.com/scofieId16/Super-Cashier/blob/a1661d9ecfb1e4acb65d0cab55eaf77fe7883a63/Flowchart/Updateharga.png)

### Flowchart Update Jumlah Item
![Update Item Quantity Flowchart](https://github.com/scofieId16/Super-Cashier/blob/a1661d9ecfb1e4acb65d0cab55eaf77fe7883a63/Flowchart/Updatejumlah.png)

### Flowchart Delete Item
![Delete an Item Flowchart](https://github.com/scofieId16/Super-Cashier/blob/a1661d9ecfb1e4acb65d0cab55eaf77fe7883a63/Flowchart/Deleteitem.png)

### Flowchart Reset Transaksi
![Delete All Items Flowchart](https://github.com/scofieId16/Super-Cashier/blob/a1661d9ecfb1e4acb65d0cab55eaf77fe7883a63/Flowchart/Resettransaksi.png)

### Flowchart Cek Keranjang
![Show Cart Flowchart](https://github.com/scofieId16/Super-Cashier/blob/a1661d9ecfb1e4acb65d0cab55eaf77fe7883a63/Flowchart/Cekkeranjang.png)

### Flowchart Total Belanja
![Calculate Total Flowchart](https://github.com/scofieId16/Super-Cashier/blob/35b4a19b779727626fcf4371af910792031e6b88/Flowchart/Totalbelanja.png)


## 4. **Penjelasan Code**

Adapun fitur-fitur atau fungsi yang dapat dijalankan pada program ini adalah :

#### input item
```python
def add_item(self):
        
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
```

Fungsi ini adalah untuk menambahkan item produk ke dalam dictionary keranjang  yang telah kita buat sebelumnya. Beberapa item yang diinput adalah : Nama Item, Jumlah Item dan Harga Item. Variabel Total harga adalah hasil dari Jumlah Item * Harga Item.

#### update nama item
```python
def update_item(self):
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
```

Fungsi ini adalah untuk melakukan update nama item jika terdapat kesalahan pada penginputan nama. Pembeli akan menginputkan nama item yang akan diubah, jika tidak ada dalam item maka akan dilakukan looping sampai nama item yang diinput ada pada keranjang terpilih. Jika nama item benar, maka akan dilakukan perubahan nama item menjadi nama item yang baru, dan delete nama item yang lama.

#### update jumlah item
```python
def update_jumlah(self):
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
```

Fungsi ini adalah untuk melakukan update jumlah item jika terdapat kesalahan pada penginputan jumlah. Pembeli akan menginputkan nama item yang akan diubah jumlahnya, jika tidak ada dalam keranjang maka akan dilakukan looping sampai nama item yang diinput ada pada keranjang terpilih. Jika nama item benar, maka selanjutnya pembeli akan menginputkan jumlah item yang baru dan mengganti jumlah item yang lama.

#### update harga item
```python
def update_harga(self):
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
```

Fungsi ini adalah untuk melakukan update harga item jika terdapat kesalahan pada penginputan harga. Pembeli akan menginputkan nama item yang akan diubah harganya, jika tidak ada dalam keranjang maka akan dilakukan looping sampai nama item yang diinput ada pada keranjang terpilih. Jika nama item benar, maka selanjutnya pembeli akan menginputkan harga item yang baru dan mengganti harga item yang lama.

#### delete item
```python
def delete_item(self):
      
    nama_item = input("Masukkan nama produk: ").capitalize()
    if nama_item in self.keranjang:
        self.keranjang.pop(nama_item)
        print(f"{nama_item} sudah dihapus dari daftar")
    else:
        print(f"{nama_item} tidak ada dalam daftar")       
```

Fungsi ini adalah untuk menghapus data salah satu item yang ada di keranjang. Pembeli akan menginputkan nama item yang akan hapus, jika tidak ada dalam keranjang maka akan dilakukan looping sampai nama item yang diinput ada pada keranjang terpilih. Jika nama item benar, maka akan menghapus item tersebut  beserta jumlah dan harganya.

#### reset transaksi
```python
def reset_transaksi(self):
          
    self.keranjang.clear()
    print("Daftar belanja telah dihapus")     
```

Fungsi ini adalah untuk menghapus data seluruh item yang ada di keranjang. Ketika customer menjalankan fungsi ini maka akan menghapus seluruh item beserta jumlah dan harganya sehingga keranjang menjadi kosong.

#### cek keranjang
```python
def cek_keranjang(self):
        
    print("\n------------ Super Cashier -------------")
    print("------------ List Transaction  ------------\n")
    if len(self.keranjang) == 0:
        print("Anda tidak memiliki item pada keranjang")
    else:
        kolom = pd.DataFrame.from_dict(self.keranjang, orient='index', columns=['Id Transaksi', 'Jumlah', 'Harga', 'Total Harga'])
        print(kolom)       
```

Fungsi ini adalah untuk menampilkan keranjang dari item yang sudah ditambahkan. Sehingga customer dapat melakukan pemeriksaan item apakah daftar belanja sudah sesuai atau belum.

#### total belanja
```python
def total_belanja(self):
        
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
```

Fungsi ini adalah untuk menampilkan total belanja yang dibeli. 

Dengan kondisional sebagai berikut. 

            a. Jika total belanja di atas Rp 200.000 akan mendapatkan diskon 5%
            b. Jika total belanja di atas Rp 300.000 akan mendapatkan diskon 8%
            c. Jika total belanja di atas Rp 500.000 akan mendapatkan dikon 10%
            d. Jika di bawah Rp 200.000 maka akan langsung menampilkan total harga belanja

Kemudian customer akan menginput uang yang disetor.

            a. Jika jumlah uang yang disetor kurang dari total harga belanja maka akan menampilkan pesan "Jumlah uang yang Anda masukkan kurang"
            b. Jika jumlah uang yang disetor sama dengan total harga belanja maka akan menampilkan pesan "Anda membayar dengan uang pas"
            c. Jika jumlah uang yang disetor lebih dari total harga belanja maka akan menampilkan pesan "Uang kembalian: Rp. "

## 5. **TEST CASE SUPER CASHIER**

### **Test 1 :**

  Customer ingin menambahkan dua item baru menggunakan method add_item(). Item yang ditambahkan adalah sebagai berikut :
      - Nama Item : Ayam Goreng, Qty : 2, Harga : 20000
      - Nama Item : Pasta Gigi, Qty : 3. Harga : 15000

  **Output :** 

![image](https://github.com/scofieId16/Super-Cashier/blob/2d9b4c351f52ec729e2ef7e0c27b4afb2950f947/Test%20Case/Testcase1.png)

### **Test 2 :**

  Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer menggunakan
  method delete_item() untuk menghapus item. item yang dihapuskan adalah **Pasta Gigi.**:
  
  **Output :**  
  
![image](https://github.com/scofieId16/Super-Cashier/blob/2d9b4c351f52ec729e2ef7e0c27b4afb2950f947/Test%20Case/Testcase2.png)

### **Test 3 :**

  Ternyata setelah dipikir-pikir Customer salah memasukkan item yang ingin dibelanjakan! 
  Daripada menghapusnya satu-satu, maka Customer cukup menggunakan method reset_keranjang() untuk menghapus semua
  item yang sudah ditambahkan:
  
  **Output :**  
  ![image](https://github.com/scofieId16/Super-Cashier/blob/2d9b4c351f52ec729e2ef7e0c27b4afb2950f947/Test%20Case/Testcase3.png)

### **Test 4 :**

  Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method total_price(). Sebelum mengeluarkan output total belanja akan menampilkan item-item yang dibeli serta menentukkan berapa diskon yang didapat customer. 
  
  **Output :**  
  ![image](https://github.com/scofieId16/Super-Cashier/blob/2d9b4c351f52ec729e2ef7e0c27b4afb2950f947/Test%20Case/Testcase4.1.png)

  **Output :**  
  ![image](https://github.com/scofieId16/Super-Cashier/blob/2d9b4c351f52ec729e2ef7e0c27b4afb2950f947/Test%20Case/Testcase4.2.png)

  **Output :**  
  ![image](https://github.com/scofieId16/Super-Cashier/blob/2d9b4c351f52ec729e2ef7e0c27b4afb2950f947/Test%20Case/Testcase4.3.png)

## 6. **CONCLUSION**

Berdasarkan requirements yang ada pada promblem case super cashier ini, seluruh requiremetns dapat dijalankan sesuai dengan yang diharapkan. Hasil ini belum sepenuhnya sempurna dan masih banyak point-point pengembangan yang dapat dikembangkan kedepannya. Untuk itu beberapa perbaikan yang dapat dilakukan jika mempunyai waktu lebih dan SDM lebih diantaranya adalah :

1. Menambahkan fitur membership atau loyalty dimana terdapat setiap level (blue,silver,gold,platinum etc) yang nantinya akan mendapatkan point setiap selesai melakukan transaksi. customer juga bisa menginput id member mereka saat ingin melakukan pembayaran.
2. Menambahkan menu untuk melihat item dan stok yang tersedia di swalayan.
3. Menggunakan Graphic User Interface agar tampilan lebih interaktif.
4. Melakukan Perbaikan dan update fitur apabila customer(user) menemukan kendala di kemudian hari.