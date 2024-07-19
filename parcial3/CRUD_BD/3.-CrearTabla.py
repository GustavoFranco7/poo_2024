from ConexionBD import *
import mysql.connector  # Importa el módulo para manejar excepciones específicas

micursor = None

try:
    if conexion.is_connected():
        micursor = conexion.cursor()
        sql = "CREATE TABLE clientes1 (id INT PRIMARY KEY AUTO_INCREMENT,nombre VARCHAR(60),direccion VARCHAR(120),telefono VARCHAR(10))"
        

        micursor.execute(sql)
        print("Se creó la tabla con éxito")
    else:
        print("No se pudo establecer la conexión a la base de datos")
except mysql.connector.Error as e:
    print(f"Ocurrió un error al crear la tabla: {e}")
    print(f"Tipo de error: {type(e).__name__}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
    print(f"Tipo de error: {type(e).__name__}")
finally:
    if micursor is not None:
        micursor.close()
    if conexion.is_connected():
        conexion.close()
