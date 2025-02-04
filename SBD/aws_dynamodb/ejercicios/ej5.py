from imports import *
from conexion import *

# 5 - Eliminar un registro de cada tabla

table = dynamodb.Table('Usuarios')
response = table.delete_item(
  Key={
    'usuario_id': '1',
  }
)
print(json.dumps(response, indent=4))

table = dynamodb.Table('Canciones')
response = table.delete_item(
  Key={
    'cancion_id': '1',
  }
)
print(json.dumps(response, indent=4))

table = dynamodb.Table('Artistas')
response = table.delete_item(
  Key={
    'artista_id': '1',
  }
)
print(json.dumps(response, indent=4))