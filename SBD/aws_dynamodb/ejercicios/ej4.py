from imports import *
from conexion import *


# Actualizar usuario
table = dynamodb.Table('Usuarios')
key = {'usuario_id': '1'}

update_expression = 'SET #nombre = :nuevo_nombre'

expression_attribute_names = {'#nombre': 'nombre_usuario'}
expression_attribute_values = {':nuevo_nombre': 'Jesusito'}

response = table.update_item(
    Key=key,
    UpdateExpression=update_expression,
    ExpressionAttributeNames=expression_attribute_names,
    ExpressionAttributeValues=expression_attribute_values
)
print("Usuario actualizado:", response)


# Actualizar cancion

table = dynamodb.Table('Canciones')
key = {'cancion_id': '1'}

update_expression = 'SET #nombre = :nuevo_nombre'

expression_attribute_names = {'#nombre': 'nombre_cancion'}
expression_attribute_values = {':nuevo_nombre': 'Beliver'}

response = table.update_item(
    Key=key,
    UpdateExpression=update_expression,
    ExpressionAttributeNames=expression_attribute_names,
    ExpressionAttributeValues=expression_attribute_values
)
print("Cancion actualizada:", response)


# Actualizar artista
table = dynamodb.Table('Artistas')
key = {'artista_id': '1'}

update_expression = 'SET #nombre = :nuevo_nombre'

expression_attribute_names = {'#nombre': 'nombre_artista'}
expression_attribute_values = {':nuevo_nombre': 'Imagine Dragons'}

response = table.update_item(
    Key=key,
    UpdateExpression=update_expression,
    ExpressionAttributeNames=expression_attribute_names,
    ExpressionAttributeValues=expression_attribute_values
)
print("Artista actualizado:", response)