from service.database import obtener_conexion

def insertar_usuario(nombre , A_Paterno , A_Materno , email , password):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(nombre , A_Paterno , A_Materno , email , password) VALUES(%s , %s, %s , %s , %s)", (nombre , A_Paterno , A_Materno , email , password))

    conexion.commit()
    conexion.close()





def obtener_nombre():
    conexion = obtener_conexion()
    nombre = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT nombre")