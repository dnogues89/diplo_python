import sqlite3

"""
el_desafio.db
(db) Tabla
Titulo
Descripcion
Ruta
"""


def conectar():
    con = sqlite3.connect("el_desafio.db")
    return con
