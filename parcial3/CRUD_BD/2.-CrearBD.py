import mysql.connector

# Conexión con la BD de MySQL
try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''  # Asegúrate de que la contraseña sea correcta
    )

    # Crear un objeto nuevo de tipo cursor para ejecutar SQL
    micursor = conexion.cursor()

    # Crear la base de datos
    sql = "CREATE DATABASE bd_python1"
    micursor.execute(sql)
except mysql.connector.Error as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print(f"Ocurrió un error")
else:
    print("Se creó la BD correctamente")
    micursor.execute("SHOW DATABASES")
    for x in micursor:
        print(x)
finally:
    if micursor:
        micursor.close()
    if conexion.is_connected():
        conexion.close()


#verificar si la conexion es correcta
#  if conexion.is_connected():
#      print(f"Se creo la conexion exitosamente")
#  else:
#      print(f"No se creo la conexion")
