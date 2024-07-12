#import ConexionBD
from ConexionBD import *

try:
    micursor=ConexionBD.conexion.cursor()
    sql="create table clientes1(id int primaty key auto_increment, nombre varchar(60),direccion varhcar(120),telefono varchar(10))"

    micursor.execute(sql)

    print("Se creo la tabla con exito")
except:
    print(f"ocurrio un error")
else:
    print("Se creo la tabla con exito")

