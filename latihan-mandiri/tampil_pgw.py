import mysql.connector
import sys

def main():
    try:
        connection = mysql.connector.connect(
        user='root', password='', host='localhost', database='db_pegawai'
        )

        sql = ("SELECT * FROM pegawai ORDER by NIP")
        try:
            mycursor = connection.cursor()
            mycursor.execute(sql)

            hasil = mycursor.fetchall()
            print("{} Data yang ditampilkan\n".format(mycursor.rowcount))

            for row in hasil:

                nip = row[0]
                nama = row[1]
                jabatan = row[2]
                divisi = row[3]
                gaji = row[4]

                # print(nip, "\t", nama, "\t", jabatan, "\t", divisi, "\t", gaji, "\t")
                print(
                "NIP       :", nip,"\nNAMA      :", nama,"\nJABATAN   :", jabatan,"\nDIVISI    :", divisi,"\nGAJI      :", gaji, "\n"
                )
        except:
            print("Menampilkan data gagal...")
            sys.exit()
        else:
            connection.close                

    except mysql.connector.Error as e:
        print("Error", e)
    else:
        connection.close

if __name__ == "__main__":
    main() 