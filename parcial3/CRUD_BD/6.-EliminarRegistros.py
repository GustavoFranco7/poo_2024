from ConexionBD import *

try:
    micursor=ConexionBD.conexion.cursor()
    sql="DELETE FROM clientes where id = 1" 

    micursor.execute(sql)
    #Es necesario ejecutar el commit para que finalice el sql con exito
    conexion.commit()#insert,update,delete
    
except:
    print(f"ocurrio un error")
else:
    print("Regitro eliminado con exito")

