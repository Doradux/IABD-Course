from imports import *
from conexion import *

class crear_tabla:
    def __init__(self, dyn_resource):
        self.dyn_resource = dyn_resource
        self.table = None


    def create_table(self, table_name, partition_key, attribute_definitions):
        try:
            table = self.dyn_resource.create_table(
                TableName=table_name,
                KeySchema=[
                    {'AttributeName': partition_key, 'KeyType': 'HASH'},
                ],
                AttributeDefinitions=attribute_definitions,
                ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
            )
            table.wait_until_exists()
            print(f"Tabla '{table_name}' creada exitosamente")
        except ClientError as e:
            print(f"Error al crear la tabla {table_name}: {e}")
