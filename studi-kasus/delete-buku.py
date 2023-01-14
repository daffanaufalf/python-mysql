import mysql.connector

dict_buku = {}

kdbuku = input("Masukkan kode buku: ")

dict_buku ['kode'] = kdbuku

nama_db = {
    'user':'root',
    'password':'',
    'host':'localhost',
    'database':'python_mysql'
    }

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

sql = ("DELETE FROM buku WHERE kode = %(kode)s")
kursor.execute(sql, dict_buku)
koneksi.commit()

print("{} data dihapus".format(kursor.rowcount))
koneksi.close