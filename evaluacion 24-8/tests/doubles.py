class VistaMock:
    def __init__(self, menu_value: int):
        self.value = menu_value
        self.mostrar_error_fue_invocado = False
        self.lista_lista_recibida = None
        self.lista_fue_invocado = False

    def menu(self):
        return self.value

    def mostrar_error(self):
        self.mostrar_error_fue_invocado = True
    
    def lista(self, lista):
        self.lista_lista_recibida = lista
        self.lista_fue_invocado = True

class RepositorioSpy:
    def __init__(self):
        self.alta_fue_invocado = False

    def alta(self, modelo, cantidad):
        self.alta_fue_invocado = True

class RepositorioMock: 
    def __init__(self, stubbed_data = []):
        self.stubbed_data = stubbed_data

    def consulta(self):
        return self.stubbed_data
