class Categoria:
    def __init__(self,IDCategoria, nombre):
        self.IDCategoria = IDCategoria
        self.nombre = nombre
        self.categorias = {}

class RegistroCategoria:
    def __init__(self):
        self.categorias = {}

    def agregarCategoria(self):
        pass