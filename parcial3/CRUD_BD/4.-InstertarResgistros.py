from ConexionBD import *

try:
    micursor=ConexionBD.conexion.cursor()
    sql="INSERT INTO clientes (id, nombre, direccion, telefono) VALUES (NULL, 'Gustavo Franco', 'col maximo gamiz', '6183701567')"

    micursor.execute(sql)
    #Es necesario ejecutar el commit para que finalice el sql con exito
    conexion.commit()#insert,update,delete

    print("Se creo la tabla con exito")
except:
    print(f"ocurrio un error")
else:
    print("Regitro insertado con exito")