import mysql.connector

def conectar():
    connection_string = None
    try:
            connection_string = mysql.connector.connect(
            user = "root",
            password = "sylvio123",
            database = "banco"
        )
    except Exception as ex:
        print(ex)
    return connection_string

def desconectar(connection_string):
    if (connection_string):
        connection_string.close()

