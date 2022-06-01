from os import curdir
import sqlite3


def crear_base():
    con = sqlite3.connect("mibase.db")
    return con


def crear_tabla(con):
    cursor = con.cursor()
    sql = "CREATE TABLE personas(id integrar PRIMARY KEY, nombre text)"
    cursor.execute(sql)
    con.commit()


def insertar(con, nombre, mi_id):
    cursor = con.cursor()
    data = (mi_id, nombre)
    sql = "INSERT INTO personas(id, nombre) VALUES (?,?)"
    cursor.execute(sql, data)
    con.commit()


def borrar(con, mi_id):
    cursor = con.cursor()
    data = (int(mi_id),)
    sql = "DELETE FROM personas WHERE id=?;"
    cursor.execute(sql, data)
    con.commit()


def update(con, mi_id, nombre):
    cursor = con.cursor()
    data = (nombre, int(mi_id))
    sql = "UPDATE personas SET nombre=? WHERE id=?;"
    cursor.execute(sql, data)
    con.commit()


def seleccionar(con, mi_id):
    cursor = con.cursor()
    data = (int(mi_id),)
    sql = "SELECT * FROM personas WHERE id=?"
    cursor.execute(sql, data)

    rows = cursor.fetchall()

    for row in rows:
        print(row)


seleccionar(crear_base(), 35)
