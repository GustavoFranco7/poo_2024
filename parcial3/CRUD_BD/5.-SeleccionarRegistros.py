from ConexionBD import *

try:
    micursor=ConexionBD.conexion.cursor()
    sql="select * from clientes"

    micursor.execute(sql)

    resultado=micursor.fetchall()

    for fila in resultado:
        print(f("id:{fila} | nombre:{fila}"))
except:
    print(f"ocurrio un error")
else:
    print("Registros consultados con exito")