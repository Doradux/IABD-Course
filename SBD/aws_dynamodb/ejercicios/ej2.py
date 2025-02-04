from conexion import *

#Crear tres registros encada tabla (0.5 puntos)

#Usuarios
table = dynamodb.Table('Usuarios')
response = table.put_item(
    Item={
        'usuario_id': '1',
        'nombre_usuario': 'Antonio',
        'correo_usuario': 'antonio@gmail.com',
    }
)

response = table.put_item(
    Item={
        'usuario_id': '2',
        'nombre_usuario': 'Marcos',
        'correo_usuario': 'marcos@gmail.com',
    }
)

response = table.put_item(
    Item={
        'usuario_id': '3',
        'nombre_usuario': 'Eduardo',
        'correo_usuario': 'eduardo@gmail.com',
    }
)

#Canciones
table = dynamodb.Table('Canciones')
response = table.put_item(
    Item={
        'cancion_id': '1',
        'nombre_cancion': 'Popy',
        'duracion': '3:00',
    }
)

response = table.put_item(
    Item={
        'cancion_id': '2',
        'nombre_cancion': 'Pobre diabla',
        'duracion': '2:00',
    }
)

response = table.put_item(
    Item={
        'cancion_id': '3',
        'nombre_cancion': 'Virtual diva',
        'duracion': '4:00',
    }
)

#Artistas
table = dynamodb.Table('Artistas')
response = table.put_item(
    Item={
        'artista_id': '1',
        'nombre_artista': 'Ariana Grande',
        'popularidad': 'alta',
    }
)

response = table.put_item(
    Item={
        'artista_id': '2',
        'nombre_artista': 'Justin Bieber',
        'popularidad': 'alta',
    }
)

response = table.put_item(
    Item={
        'artista_id': '3',
        'nombre_artista': 'El Alfa el Jefe',
        'popularidad': 'altisima',
    }
)