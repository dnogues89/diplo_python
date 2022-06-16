import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import *
import datetime
import os
import re

# Intentar agregarle color por margen.
# Falta hacer un validador de 1 campo
# Intentar transformarla en un ejecutable.

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))

today = datetime.date.today()


def conexion():
    con = sqlite3.connect(os.path.join(BASE_DIR, "mi_proyecto.db"))

    return con


def nueva_tabla():
    con = conexion()
    cursor = con.cursor()
    sql = "CREATE TABLE IF NOT EXISTS listaprecios(codigo INTEGER PRIMARY KEY,modelo,lista real,venta real)"
    cursor.execute(sql)
    con.commit()


# ==========MODELO==========
def alta(ecodigo, emodelo, elista, eventa, tree):
    patron = "[0-9]+"

    if re.match(patron, ecodigo.get()):
        con = conexion()
        cursor = con.cursor()
        data = (int(ecodigo.get()), emodelo.get(), elista.get(), eventa.get())
        sql = "INSERT INTO listaprecios(codigo, modelo, lista,venta) VALUES (?,?,?,?)"
        cursor.execute(sql, data)
        con.commit()
        actualizar_treeview(tree)

    else:
        messagebox.showerror(
            title="Error en el codigo", message="El codigo solo debe contener Numeros"
        )


def baja(tree):
    eliminar = tree.selection()
    item = tree.item(eliminar)
    codigo = item["text"]

    con = conexion()
    cursor = con.cursor()
    data = (codigo,)
    sql = "DELETE FROM listaprecios WHERE codigo = ?"
    cursor.execute(sql, data)
    con.commit()
    actualizar_treeview(tree)


def modificar(ecodigo, emodelo, elista, eventa, tree):
    consulta = tree.selection()
    item = tree.item(consulta)
    codigo = item["text"]

    if askyesno("Continuar", "Desea modificar el codigo " + str(codigo)):
        con = conexion()
        cursor = con.cursor()
        data = (emodelo.get(), elista.get(), eventa.get(), codigo)
        sql = "UPDATE listaprecios SET modelo=?, lista=?, venta=? WHERE codigo=?;"
        cursor.execute(sql, data)
        con.commit()
        actualizar_treeview(tree)


def consulta(tree):
    consulta = tree.selection()
    item = tree.item(consulta)
    codigo = item["text"]
    modelo = item["values"][0]
    precio_lista = item["values"][1]
    precio_venta = item["values"][2]

    showinfo(
        title=f"Margen {modelo}",
        message=f"El margen de {modelo} es {round((float(precio_venta)/float(precio_lista)-1)*100,0)}%",
    )


def actualizar_treeview(mitreview):
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    sql = "SELECT * FROM listaprecios ORDER BY Codigo ASC"
    con = conexion()
    cursor = con.cursor()
    datos = cursor.execute(sql)

    resultado = datos.fetchall()
    for fila in resultado:
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))


window = Tk()
nueva_tabla()

# ==========VISTA==========
window.title("Lista de precios para mes: " + str(today.month) + "/" + str(today.year))

# ==========Labels=========
# Intento de regex
parametros = "[0-9]"
lcodigo = Label(window, text="Código")
lcodigo.grid(row=1, column=2, sticky=E)

lmodelo = Label(window, text="Modelo")
lmodelo.grid(row=2, column=2, sticky=E)

lpreciolista = Label(window, text="Precio Lista")
lpreciolista.grid(row=1, column=4, sticky=E)

lprecioventa = Label(window, text="Precio Venta")
lprecioventa.grid(row=2, column=4, sticky=E)

# =========Entry==========
v_codigo, v_modelo, v_lista, v_venta, v_margen = (
    IntVar(),
    StringVar(),
    IntVar(),
    IntVar(),
    DoubleVar(),
)


ecodigo = Entry(window, textvariable=v_codigo, width=5)
ecodigo.grid(row=1, column=3, sticky=W)


emodelo = Entry(window, textvariable=v_modelo)
emodelo.grid(row=2, column=3, sticky=W)

elista = Entry(window, textvariable=v_lista)
elista.grid(row=1, column=5, sticky=W)

eventa = Entry(window, textvariable=v_venta)
eventa.grid(row=2, column=5, sticky=W)

# ========== TREEVIEW ==========
tree = ttk.Treeview(window)
tree["columns"] = ("col1", "col2", "col3")
tree.column("#0", width=50, anchor="c")
tree.column("col1", width=200, anchor="c")
tree.column("col2", width=200, anchor="c")
tree.column("col3", width=200, anchor="c")


tree.heading("#0", text="ID")
tree.heading("col1", text="Modelo")
tree.heading("col2", text="$ Lista")
tree.heading("col3", text="$ Venta")

tree.grid(row=4, column=1, columnspan=5)

actualizar_treeview(tree)
# ==========Botones==========

balta = Button(
    window,
    text="Alta",
    command=lambda: alta(ecodigo, emodelo, elista, eventa, tree),
)
balta.grid(row=3, column=2)

bbaja = Button(window, text="Baja", command=lambda: baja(tree))
bbaja.grid(row=3, column=3)

bmodificar = Button(
    window,
    text="Modificar",
    command=lambda: modificar(ecodigo, emodelo, elista, eventa, tree),
)
bmodificar.grid(row=3, column=4)

bconsulta = Button(window, text="Consulta", command=lambda: consulta(tree))
bconsulta.grid(row=3, column=5)


window.mainloop()
