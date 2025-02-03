from imports import *
from conexion import *

class anadir_registro:
    def __init__(self, dyn_resource):
        self.dyn_resource = dyn_resource


    def anadir_registro(self, params, nombre_tabla):
        table = self.dyn_resource.Table(nombre_tabla)
        try:
            table.put_item(Item=params)
        except ClientError as err:
            logger.error(
                "Couldn't add data %s to table %s. Here's why: %s: %s",
                table.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise


