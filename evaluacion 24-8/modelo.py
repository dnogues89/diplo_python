from peewee import *
import re

try:
    db = SqliteDatabase("stock_vw.db")
    # Declarar que base voy a utilizar
    class BaseStock(Model):
        class Meta:
            database = db

    # Defino el modelo con peewee
    class Stock(BaseStock):
        modelo = CharField()
        cantidad = IntegerField()

    db.connect()
    db.create_tables([Stock])

except:
    print("No se puede conectar con la base de datos.")


class Repositorio:
    def alta(modelo, cantidad):
        alta = Stock()
        alta.modelo = modelo
        alta.cantidad = cantidad
        alta.save()
        return alta

    def baja(id):
        baja = Stock.get(Stock.id == id)
        baja.delete_instance()
        return True

    def modificar(id, modelo, cantidad):
        modificar = Stock.update(modelo=modelo, cantidad=cantidad).where(Stock.id == id)
        modificar.execute()
        return True

    def consulta():
        lista = []
        for row in Stock.select():
            lista.append([row.id, row.modelo, row.cantidad])

        return lista
