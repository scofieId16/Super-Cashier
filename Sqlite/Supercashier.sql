PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE transaksi_supercashier (
                    new_id_transaksi VARCHAR(20) PRIMARY KEY,
                    tanggal_transaksi DATETIME,
                    nama_pelanggan TEXT,
                    nama_item TEXT,
                    jumlah_item INTEGER,
                    harga INTEGER,
                    total_harga INTEGER,
                    diskon REAL,
                    harga_diskon INTEGER
                );
INSERT INTO transaksi_supercashier VALUES('80370706_01','10-08-2023 22:53:59','Ahmad faisal fahmi','Ayam goreng',2,20000,40000,0.050000000000000002775,38000);
INSERT INTO transaksi_supercashier VALUES('80370706_02','10-08-2023 22:53:59','Ahmad faisal fahmi','Pasta gigi',3,15000,45000,0.050000000000000002775,42750);
INSERT INTO transaksi_supercashier VALUES('80370706_03','10-08-2023 22:53:59','Ahmad faisal fahmi','Mainan mobil',1,200000,200000,0.050000000000000002775,190000);
INSERT INTO transaksi_supercashier VALUES('80370706_04','10-08-2023 22:53:59','Ahmad faisal fahmi','Mi instan',5,3000,15000,0.050000000000000002775,14250);
COMMIT;

SELECT * FROM transaksi_supercashier