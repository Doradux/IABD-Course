from imports import *
from conexion import *

# 3 - Obtener un registro de cada tabla (1 punto)

tables = [dynamodb.Table('Usuarios'), dynamodb.Table('Canciones'), dynamodb.Table('Artistas')]

for table in tables:
    response = table.scan()
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    print(json.dumps(data[0], indent=4))