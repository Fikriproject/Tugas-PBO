import sqlite3
from tkinter import *
from tkinter import filedialog
import mysql.connector

def convert_sqlite_to_mysql(sqlite_file, mysql_host, mysql_user, mysql_password, mysql_database):
    try:
        # Koneksi ke SQLite
        sqlite_connection = sqlite3.connect(sqlite_file)
        sqlite_cursor = sqlite_connection.cursor()

        # Koneksi ke MySQL
        mysql_connection = mysql.connector.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_password,
            database=mysql_database
        )
        mysql_cursor = mysql_connection.cursor()

        # Dapatkan tabel dari SQLite
        sqlite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = sqlite_cursor.fetchall()

        for table in tables:
            table_name = table[0]
            
            # Pengecekan khusus untuk tabel 'sqlite_sequence'
            if table_name == 'sqlite_sequence':
                continue

            sqlite_cursor.execute(f"SELECT * FROM {table_name}")
            rows = sqlite_cursor.fetchall()

            # Buat tabel di MySQL jika belum ada
            create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} AS SELECT * FROM {table_name} LIMIT 0"
            mysql_cursor.execute(create_table_query)

            # Masukkan data ke MySQL
            mysql_cursor.executemany(f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(rows[0]))})", rows)

        # Commit dan tutup koneksi
        mysql_connection.commit()
        print("Konversi berhasil!")

    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

    finally:
        mysql_connection.close()
        sqlite_connection.close()

def choose_sqlite_file():
    file_path = filedialog.askopenfilename(filetypes=[("SQLite files", "*.db;*.sqlite;*.db3")])
    sqlite_file_entry.delete(0, END)
    sqlite_file_entry.insert(0, file_path)

def convert_button_clicked():
    sqlite_file = sqlite_file_entry.get()
    mysql_host = mysql_host_entry.get()
    mysql_user = mysql_user_entry.get()
    mysql_password = mysql_password_entry.get()
    mysql_database = mysql_database_entry.get()

    convert_sqlite_to_mysql(sqlite_file, mysql_host, mysql_user, mysql_password, mysql_database)

# Membuat GUI
root = Tk()
root.title("SQLite to MySQL Converter")

# Label dan Entry untuk SQLite file
sqlite_file_label = Label(root, text="SQLite File:")
sqlite_file_label.grid(row=0, column=0, padx=10, pady=10)

sqlite_file_entry = Entry(root, width=40)
sqlite_file_entry.grid(row=0, column=1, padx=10, pady=10)

choose_button = Button(root, text="Choose", command=choose_sqlite_file)
choose_button.grid(row=0, column=2, padx=10, pady=10)

# Label dan Entry untuk MySQL
mysql_host_label = Label(root, text="MySQL Host:")
mysql_host_label.grid(row=1, column=0, padx=10, pady=10)

mysql_host_entry = Entry(root, width=40)
mysql_host_entry.grid(row=1, column=1, padx=10, pady=10)

mysql_user_label = Label(root, text="MySQL User:")
mysql_user_label.grid(row=2, column=0, padx=10, pady=10)

mysql_user_entry = Entry(root, width=40)
mysql_user_entry.grid(row=2, column=1, padx=10, pady=10)

mysql_password_label = Label(root, text="MySQL Password:")
mysql_password_label.grid(row=3, column=0, padx=10, pady=10)

mysql_password_entry = Entry(root, width=40, show="*")
mysql_password_entry.grid(row=3, column=1, padx=10, pady=10)

mysql_database_label = Label(root, text="MySQL Database:")
mysql_database_label.grid(row=4, column=0, padx=10, pady=10)

mysql_database_entry = Entry(root, width=40)
mysql_database_entry.grid(row=4, column=1, padx=10, pady=10)

# Tombol Convert
convert_button = Button(root, text="Convert", command=convert_button_clicked)
convert_button.grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()
