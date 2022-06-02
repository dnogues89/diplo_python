from tkinter import *
from tkinter.tix import COLUMN

# ==========MODELO==========
def alta():
    pass


def baja():
    pass


def modificar():
    pass


def consulta():
    pass


window = Tk()


# ==========VISTA==========
window.title("Lista de precios")

# ==========Labels=========
lcodigo = Label(window, text="Código")
lcodigo.grid(row=1, column=2)

lmodelo = Label(window, text="Modelo")
lmodelo.grid(row=2, column=2)

lpreciolista = Label(window, text="Precio Lista")
lpreciolista.grid(row=1, column=4)

lprecioventa = Label(window, text="Precio Venta")
lprecioventa.grid(row=2, column=4)

# =========Entry==========
v_codigo, v_modelo, v_lista, v_venta, v_margen = (
    IntVar(),
    StringVar(),
    IntVar(),
    IntVar(),
    DoubleVar(),
)

ecodigo = Entry(window, textvariable=v_codigo)
ecodigo.grid(row=1, column=3)

emodelo = Entry(window, textvariable=v_modelo)
emodelo.grid(row=2, column=3)

elista = Entry(window, textvariable=v_lista)
elista.grid(row=1, column=5)

eventa = Entry(window, textvariable=v_venta)
eventa.grid(row=2, column=5)

# ==========Botones==========

balta = Button(
    window, text="Alta", command=lambda: alta(ecodigo, emodelo, elista, eventa)
)
balta.grid(row=3, column=2)

bbaja = Button(
    window, text="Baja", command=lambda: baja(ecodigo, emodelo, elista, eventa)
)
bbaja.grid(row=3, column=3)

bmodificar = Button(
    window,
    text="Modificar",
    command=lambda: modificar(ecodigo, emodelo, elista, eventa),
)
bmodificar.grid(row=3, column=4)

bconsulta = Button(window, text="Consulta", command=lambda: consulta())
bconsulta.grid(row=3, column=5)


window.mainloop()
