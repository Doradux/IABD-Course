from imports import *
from conexion import *

# 9 - Obtener un conjunto de datos a través de varios filtros aplicado en cada tabla

table = dynamodb.Table('Usuarios')

response = table.scan(
    FilterExpression=Attr('nombre_usuario').begins_with('Ma') & Attr('correo_usuario').contains('gmail')
)

print("The query returned the following items:")
for item in response['Items']:
    print(json.dumps(item, indent=4))
