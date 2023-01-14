import mysql.connector

dict_pegawai = {}

nip = input('Masukkan NIP Anda: ')
nama = input('Masukkan nama Anda: ')
jabatan = input('Masukkan jabatan Anda: ')
divisi = input('Masukkan divisi Anda: ')
gaji = int(input('Masukkan gaji Anda: '))

dict_pegawai ['NIP'] = nip
dict_pegawai ['NAMA'] = nama
dict_pegawai ['JABATAN'] = jabatan
dict_pegawai ['DIVISI'] = divisi
dict_pegawai ['GAJI'] = gaji

db_name = {
    'user':'root',
    'password':'',
    'host':'localhost',
    'database':'db_pegawai'
    }

connection = mysql.connector.connect(**db_name)
mycursor = connection.cursor()

sql = ("UPDATE pegawai SET NAMA = %(NAMA)s , JABATAN = %(JABATAN)s , DIVISI = %(DIVISI)s , GAJI = %(GAJI)s WHERE NIP = %(NIP)s")

mycursor.execute(sql, dict_pegawai)
connection.commit()
print("{} Data berhasil diubah".format(mycursor.rowcount))

mycursor.close()
connection.close()