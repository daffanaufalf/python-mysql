import mysql.connector

dict_pegawai = {}

nip = input('Masukkan NIP Anda: ')

dict_pegawai ['NIP'] = nip

db_name = {
    'user':'root',
    'password':'',
    'host':'localhost',
    'database':'db_pegawai'
    }

connection = mysql.connector.connect(**db_name)
mycursor = connection.cursor()

sql = ("DELETE FROM pegawai WHERE NIP = %(NIP)s")

mycursor.execute(sql, dict_pegawai)
connection.commit()
print("{} Data berhasil dihapus".format(mycursor.rowcount))

mycursor.close()
connection.close()