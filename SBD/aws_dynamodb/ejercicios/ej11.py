from imports import *
from conexion import *

# 11 - Crear un backup de todas las tablas

dynamodb = boto3.client(
    'dynamodb',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    aws_session_token=aws_session_token,
    region_name=aws_region
)

response = dynamodb.create_backup(
    TableName='Usuarios',
    BackupName='Usuarios-Backup-01'
)
print(response)