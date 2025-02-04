from imports import *
from conexion import *

table = dynamodb.Table('Usuarios')

response = table.delete_item(
    Key={
        'usuario_id': '10'
    },
    ConditionExpression="attribute_exists(nombre_usuario)"
)

table = dynamodb.Table('Canciones')

response = table.delete_item(
    Key={
        'cancion_id': '2'
    },
    ConditionExpression="attribute_exists(nombre_cancion)"
)

table = dynamodb.Table('Artistas')

response = table.delete_item(
    Key={
        'artista_id': '2'
    },
    ConditionExpression="attribute_exists(nombre_artista)"
)