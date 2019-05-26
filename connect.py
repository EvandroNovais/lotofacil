import mysql.connector as connector

def connectar():
    conn = connector.connect(
        user='root', 
        password='7431282', 
        host='localhost', 
        database='loteria'
    )
    return conn
