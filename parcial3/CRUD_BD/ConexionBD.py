import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='', 
        database='bd_python'
    )
    if conexion.is_connected():
        print("Se creó la conexión exitosamente")
        conexion.close()
    else:
        print("No se creó la conexión")
except mysql.connector.Error as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print(f"Ocurrió un error")

