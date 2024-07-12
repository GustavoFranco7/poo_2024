import mysql.connector

#Conexion con la BD de MySQL
try:
    conexion=mysql.connector.connect(
        localhost='localhost',
        user='root',
        pasword=''
)

    #Crear un objeto nuevo de tipo cursor para ejecutar SQL
    micursor=conexion.cursor()

    sql="create database bd_python1"

    micursor.execute(sql)

except Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print(f"Ocurrio un error")
else:
    print("Se creo la BD correctamente")
    micursor.execute("show databases")
    for x in micursor:
        print(x)

#verificar si la conexion es correcta
#  if conexion.is_connected():
#      print(f"Se creo la conexion exitosamente")
#  else:
#      print(f"No se creo la conexion")
