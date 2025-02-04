from imports import *
from conexion import *

# 6 - Obtener todos los registros de cada tabla

tables = [dynamodb.Table('Usuarios'), dynamodb.Table('Canciones'), dynamodb.Table('Artistas')]

for table in tables:
    response = table.scan()
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    
    print("=================", table.name, "===================")
    for item in data:
        print(json.dumps(item, indent=4))