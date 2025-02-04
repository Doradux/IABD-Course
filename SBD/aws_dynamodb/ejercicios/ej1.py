from conexion import *
from funciones.crear_tabla import *

table = crear_tabla(dynamodb)
table.create_table(
    table_name="Usuarios",
    partition_key="usuario_id",
    attribute_definitions=[
        {
            'AttributeName': 'usuario_id',
            'AttributeType': 'S'  # Tipo String
        }
    ]
)

table.create_table(
    table_name="Artistas",
    partition_key="artista_id",
    attribute_definitions=[
        {
            'AttributeName': 'artista_id',
            'AttributeType': 'S'
        }
    ]
)

table.create_table(
    table_name="Canciones",
    partition_key="cancion_id",
    attribute_definitions=[
        {
            'AttributeName': 'cancion_id',
            'AttributeType': 'S'
        }
    ]
)