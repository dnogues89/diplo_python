from cgitb import text
from tkinter import *
import random
import ambc
from tkinter import ttk

from debugpy import configure


window = Tk()
# window.geometry("450x200")

# INFO LABEL + ENTRYS ========================
window.title("Ejercicio Desafio")

label_pretitulo = Label(window, text="Ingrese sus datos", bg="pink")
label_pretitulo.grid(row=0, column=1)

label_titulo = Label(window, text="Titulo")
label_titulo.grid(row=2, column=0, sticky=W)

text_titulo = Entry(window)
text_titulo.grid(row=2, column=1)

label_ruta = Label(window, text="Ruta")
label_ruta.grid(row=3, column=0, sticky=W)

text_ruta = Entry(window)
text_ruta.grid(row=3, column=1)

label_desc = Label(window, text="Descripcíon")
label_desc.grid(row=4, column=0, sticky=W)

text_desc = Entry(window)
text_desc.grid(row=4, column=1)

label_id = Label(window, text="Id")
label_id.grid(row=1, column=0, sticky=W)

text_id = Entry(window, text="No completar en altas")
text_id.grid(row=1, column=1)
# INFO LABEL + ENTRYS ========================


# BOTONES ================================
def alta_but():
    titulo = StringVar()
    titulo = text_titulo.get()

    desc = StringVar()
    desc = text_desc.get()
    ruta = StringVar()
    ruta = text_ruta.get()
    ambc.alta(titulo, ruta, desc)


but_alta = Button(window, text="Alta", command=alta_but)
but_alta.grid(row=1, column=2)


def sorpresa():
    color = random.choice(["yellow", "blue", "red", "white"])
    window.configure(bg=color)
    label_desc.configure(bg=color)
    label_pretitulo.configure(bg=color)
    label_ruta.configure(bg=color)
    label_titulo.configure(bg=color)
    but_alta.configure(bg=color)
    but_sorpresa.configure(bg=color)


but_sorpresa = Button(window, text="Sorpresa", command=sorpresa)
but_sorpresa.grid(row=6, column=1)


def baja_but():
    pass


but_baja = Button(window, text="Baja", command=baja_but)
but_baja.grid(row=2, column=2)


def mod_but():
    pass


but_mod = Button(window, text="Modificar", command=mod_but)
but_mod.grid(row=3, column=2, sticky=W)


def consulta_but():
    id = IntVar()
    id = text_id.get()
    info = ambc.consulta(id)
    tree.clipboard_clear()
    tree.insert(
        "", "end", text=(info[0][0]), values=(info[0][1], info[0][2], info[0][3])
    )


but_consulta = Button(window, text="Consulta", command=consulta_but)
but_consulta.grid(row=4, column=2)
# BOTONES ================================

# TREE ===================================

tree = ttk.Treeview(window)
tree["columns"] = ("col1", "col2", "col3")
tree.column("#0", width=50, anchor=CENTER)
tree.column("col1", width=100, anchor=CENTER)
tree.column("col2", width=100, anchor=CENTER)
tree.column("col3", width=100, anchor=CENTER)
tree.heading("#0", text="id")
tree.heading("col1", text="Titulo")
tree.heading("col2", text="Ruta")
tree.heading("col3", text="Descripcion")


tree.grid(column=0, row=6, columnspan=5)

# TREE ===================================

window.mainloop()
