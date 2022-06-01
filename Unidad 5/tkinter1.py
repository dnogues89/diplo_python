from tkinter import *

root = Tk()

e = Entry(root)
e.pack()

##############

a = 4
b = 5
c = a + b
d = "mi resultado es: " + str(c)
##############

var = IntVar()
e.config(textvariable=var)
var.set(d)


root.mainloop()
