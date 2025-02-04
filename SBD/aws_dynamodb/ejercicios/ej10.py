from imports import *
from conexion import *

dynamodb = boto3.client(
    'dynamodb',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    aws_session_token=aws_session_token,
    region_name=aws_region
)

tablas = ["Usuarios", "Artistas", "Canciones"]

for tabla in tablas:
    response = dynamodb.execute_statement(
        Statement=f'SELECT * FROM "{tabla}"'
    )

    items = response.get('Items', [])
    print(f"\n================ {tabla} ===============")
    for item in items:
        print(json.dumps(item, indent=4))
