from imports import *
from conexion import *

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