from unicodedata import category

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre


class RegistroCategoria:
    def __init__(self):
        self.categorias = {}

    def agregarCategoria(self):
        self.categorias[1] = Categoria("Categoria 1")
