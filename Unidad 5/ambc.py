import bdatos


def alta(titulo, ruta, desc):
    con = bdatos.conectar()
    cursor = con.cursor()
    data = (titulo, ruta, desc)
    sql = "INSERT INTO db(Titulo, Ruta, Descripcion) VALUES (?,?,?)"
    cursor.execute(sql, data)
    con.commit()


def baja():
    pass


def modificacion():
    pass


def consulta(id):
    con = bdatos.conectar()
    cursor = con.cursor()
    data = (id,)
    sql = "SELECT * FROM db WHERE id=?"
    cursor.execute(sql, data)
    info = cursor.fetchall()
    return info


print(consulta(9)[0][1])
