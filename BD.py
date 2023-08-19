import sys
import pyodbc
conn= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\PC 1\Downloads\bdprueba.accdb;")
cursor=conn.cursor()
cursor.execute("SELECT * FROM Tabla1")
for row in cursor.fetchall():
    print(row)
cursor.close
conn.close