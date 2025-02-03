from conexion import *
from funciones.anadir_registro import *

#Crear tres registros encada tabla (0.5 puntos)

anadir = anadir_registro(dynamodb)

params = {"nombre_usuario": "Juan"}

anadir.anadir_registro(params, "Usuarios")