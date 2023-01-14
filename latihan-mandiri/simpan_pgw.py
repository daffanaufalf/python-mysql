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

db_name = mysql.connector.connect(user='root', host='localhost', database='db_pegawai')
mycursor = db_name.cursor()

sql = ("INSERT INTO pegawai (NIP, NAMA, JABATAN, DIVISI, GAJI) VALUES (%(NIP)s, %(NAMA)s ,%(JABATAN)s ,%(DIVISI)s ,%(GAJI)s)")

mycursor.execute(sql, dict_pegawai)
db_name.commit()
print("{} Data berhasil ditambahkan".format(mycursor.rowcount))

mycursor.close()
db_name.close()