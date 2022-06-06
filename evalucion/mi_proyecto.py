import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

import datetime

mes = datetime.date.today()
print(mes.month)


def conexion():
    con = sqlite3.connect("mi_proyecto.db")
    return con


def nueva_tabla():
    con = conexion()
    cursor = con.cursor()
    sql = "CREATE TABLE listaprecios IF NOT EXIST(codigo INTEGER PRIMARY KEY AUTOINCREMENT,modelo,lista real,venta real)"
    cursor.execute(sql)
    con.commit()


# ==========MODELO==========
def alta(ecodigo, emodelo, elista, eventa):
    con = conexion()
    cursor = con.cursor()
    data = (emodelo.get(), elista.get(), eventa.get())
    sql = "INSERT INTO listaprecios(modelo, lista,venta) VALUES (?,?,?)"
    cursor.execute(sql, data)
    con.commit()


def baja(ecodigo):
    con = conexion()
    cursor = con.cursor()
    data = (ecodigo.get(),)
    sql = "DELETE FROM listaprecios WHERE codigo = ?"
    cursor.execute(sql, data)
    con.commit()


def modificar():
    pass


def consulta (ecodigo.get()):
    con = conexion()
    cursor = con.cursor()
    data = (ecodigo,)
    sql = "SELECT * FROM listaprecios WHERE codigo=?"
    cursor.execute(sql,data)
    info = cursor.fetchall(sql,data)
    print (type(info))
    print (info)

    


"""
    margen = (
        f"El Margen de {modelo} para la lista vigente es de: {round(venta/lista,0)}%"
    )
    showinfo(margen)
    pass
"""
def load_treeview():pass



window = Tk()


# ==========VISTA==========
window.title("Lista de precios para mes: " + str(mes.month))

# ==========Labels=========
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

# ==========Botones==========

balta = Button(
    window, text="Alta", command=lambda: alta(ecodigo, emodelo, elista, eventa)
)
balta.grid(row=3, column=2)

bbaja = Button(window, text="Baja", command=lambda: baja(ecodigo))
bbaja.grid(row=3, column=3)

bmodificar = Button(
    window,
    text="Modificar",
    command=lambda: modificar(ecodigo, emodelo, elista, eventa),
)
bmodificar.grid(row=3, column=4)

bconsulta = Button(window, text="Consulta", command=lambda: consulta(ecodigo))
bconsulta.grid(row=3, column=5)

# ========== TREEVIEW ==========
tree = ttk.Treeview(window)
tree["columns"] = ("col1", "col2", "col3")
tree.column("#0", width=50)
tree.column("col1", width=200)
tree.column("col2", width=200)
tree.column("col3", width=200)

tree.heading("#0", text="ID")
tree.heading("col1", text="Modelo")
tree.heading("col2", text="$ Lista")
tree.heading("col3", text="$ Venta")

tree.grid(row=4, column=1, columnspan=5)


window.mainloop()
