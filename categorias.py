class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Nombre Categoria: {self.nombre}"


class RegistroCategoria:
    def __init__(self):
        self.categorias = {}

    def agregarCategoria(self, producto):
        self.categorias[1] = {
            "Categoria": Categoria("s"),
            "Producto": producto
        }
        for c,d in self.categorias.items():
            print(c,d["Categoria"],d["Producto"])