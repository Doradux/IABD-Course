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
        # {
        #     'AttributeName': 'nombre_usuario',
        #     'AttributeType': 'S'  # Tipo String
        # },
        # {
        #     'AttributeName': 'correo',
        #     'AttributeType': 'S'  # Tipo String
        # }
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
        # {
        #     'AttributeName': 'nombre_artista',
        #     'AttributeType': 'S'
        # },
        # {
        #     'AttributeName': 'genero_principal',
        #     'AttributeType': 'S'
        # },
        # {
        #     'AttributeName': 'edad',
        #     'AttributeType': 'N'
        # }
    ]
)

table.create_table(
    table_name="Cancion",
    partition_key="cancion_id",
    attribute_definitions=[
        {
            'AttributeName': 'cancion_id',
            'AttributeType': 'S'
        }
        # {
        #     'AttributeName': 'nombre_cancion',
        #     'AttributeType': 'S'
        # },
        # {
        #     'AttributeName': 'duracion',
        #     'AttributeType': 'N'
        # },
        # {
        #     'AttributeName': 'genero_principal',
        #     'AttributeType': 'S'
        # }
    ]
)