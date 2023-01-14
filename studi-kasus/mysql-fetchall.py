import mysql.connector
import sys

def main():
    try:
        koneksi = mysql.connector.connect(
        user='root', password='', host='localhost', database='python_mysql'
        )

        sql = ("SELECT * FROM buku ORDER by kode")
        try:
            kursor = koneksi.cursor()
            kursor.execute(sql)

            hasil = kursor.fetchall()
            print("{} data yang diambil".format(kursor.rowcount))

            for row in hasil:

                kode = row[0]
                judul = row[1]
                harga = row[2]
                penerbit = row[3]
                tahun = row[4]

                print(kode, "\t", judul, "\t", harga, "\t", penerbit, "\t", tahun, "\t")
        except:
            print("Pengambilan data gagal...")
            sys.exit()
        else:
            koneksi.close                

    except mysql.connector.Error as e:
        print("Error", e)
    else:
        koneksi.close

if __name__ == "__main__":
    main() 