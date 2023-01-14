import mysql.connector
dict_buku = {}

kdbuku = input("Masukkan kode buku: ")
judul = input("Masukkan judul buku: ")
harga = int (input("Masukkan harga buku: "))
penerbit = input("Masukkan penerbit: ")
tahun = int(input("Masukkan tahun terbit: "))

dict_buku ['kode'] = kdbuku
dict_buku ['judul'] = judul
dict_buku ['harga'] = harga
dict_buku ['penerbit'] = penerbit
dict_buku ['tahun'] = tahun

nama_db = {
    'user':'root',
    'password':'',
    'host':'localhost',
    'database':'python_mysql'
    }

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

sql = ("INSERT INTO buku(kode, judul, harga, penerbit, tahun) VALUES (%(kode)s, %(judul)s, %(harga)s, %(penerbit)s, %(tahun)s)")
kursor.execute(sql, dict_buku)
koneksi.commit()

print("{} data ditambahkan".format(kursor.rowcount))
koneksi.close
