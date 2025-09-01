from productos import *

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Nombre Categoria: {self.nombre}"


class RegistroCategoria:
    def __init__(self):
        self.categorias = {}

    def agregarCategoria(self, producto):
        nombre = input("Ingrese el nombre de la categoria: ")
        id = int(input("Ingrese la id de la categoria: "))
        c = Categoria(nombre)
        self.categorias[id] = {
            "Categoria": c,
            "Producto": []
        }
        self.categorias[id]["Producto"].append(producto)
        self.categorias[id]["Producto"].append(Producto("Hola",2,3))
        for c,d in self.categorias.items():
            print(c,d["Categoria"])
            for d2 in d["Producto"]:
                print(d2)