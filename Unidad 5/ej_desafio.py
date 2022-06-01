from cgitb import text
from distutils import text_file
from tkinter import *
import random
from turtle import bgcolor

from debugpy import configure


window = Tk()
window.geometry("680x200")


window.title("Ejercicio Desafio")

label_pretitulo = Label(window, text="Ingrese sus datos", bg="pink")
label_pretitulo.grid(row=0, column=1, sticky=W, padx=380 / 2)

label_titulo = Label(window, text="Titulo")
label_titulo.grid(row=1, column=0, sticky=W)

text_titulo = Entry(window)
text_titulo.grid(row=1, column=1)

label_ruta = Label(window, text="Ruta")
label_ruta.grid(row=2, column=0, sticky=W)

text_ruta = Entry(window)
text_ruta.grid(row=2, column=1)

label_desc = Label(window, text="Descripíon")
label_desc.grid(row=3, column=0, sticky=W)

text_desc = Entry(window)
text_desc.grid(row=3, column=1)


def alta():

    print(
        f"Nueva alta de datos:\n{text_titulo.get()} {text_ruta.get()} {text_desc.get()}"
    )


but_alta = Button(window, text="Alta", command=alta)
but_alta.grid(row=4, column=1)


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
but_sorpresa.grid(row=4, column=2, sticky=W)


window.mainloop()
