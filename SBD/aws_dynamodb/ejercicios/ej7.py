from imports import *
from conexion import *

# 7 - Obtener una conjunto de registros de un filtrado de cada tabla

table = dynamodb.Table('Usuarios')

response = table.put_item(
    Item={
        'usuario_id': '10',
        'nombre_usuario': 'Maria',
        'correo_usuario': 'maria@gmail.com',
    }
)

response = table.put_item(
    Item={
        'usuario_id': '9',
        'nombre_usuario': 'Manuela',
        'correo_usuario': 'manuela@gmail.com',
    }
)

response = table.scan(
  FilterExpression=Attr('nombre_usuario').begins_with('Ma'),
)

print("The query returned the following items:")
for item in response['Items']:
  print(json.dumps(item, indent=4))