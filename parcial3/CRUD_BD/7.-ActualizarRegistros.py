from ConexionBD import *

try:
    micursor=ConexionBD.conexion.cursor()
    sql="UPDATE clientes set direccion='col UTD' where id=1" 

    micursor.execute(sql)
    #Es necesario ejecutar el commit para que finalice el sql con exito
    conexion.commit()#insert,update,delete
    
except:
    print(f"ocurrio un error")
else:
    print("Regitro actualizado con exito")

