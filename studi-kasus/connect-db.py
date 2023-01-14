import mysql.connector
from mysql.connector import errorcode

nama_db = {
    'user':'root',
    'password':'',
    'host':'localhost',
    'database':'python_mysql'
    }

try:
    nama_db = {
    'user':'root',
    'password':'',
    'host':'localhost',
    'database':'python_mysql'
    }

    koneksi = mysql.connector.connect(**nama_db)

    if koneksi.is_connected() :
        print("Koneksi database berhasil dilakukan")
    else:
        print("Koneksi database gagal dilakukan")   


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Gagal koneksi database, Kesalahan mungkin pada username atau password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Gagal koneksi database, Nama database tidak ditemukan")
    else:
        print("Tidak terhubung ke database")
