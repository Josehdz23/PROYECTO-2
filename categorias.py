from productos import Producto

categorias = {}
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Nombre Categoria: {self.nombre}"


class RegistroCategoria:
    def agregarCategoria(self,id,producto,cantidad):
        b = 0
        if id in categorias:
            for obj in categorias[id]["productos"]:
                if obj.nombre == producto.nombre:
                    obj.stock += cantidad
                    b = 1
                    return categorias[id]["nombre"].nombre
            if b == 0:
                categorias[id]["productos"].append(producto)
                return categorias[id]["nombre"].nombre
        else:
            nombre = input("La categoria no existía pero se creará, ingrese el nombre del categoría: ")
            producto.categoria = nombre
            categorias[id] = {
                "nombre": Categoria(nombre),
                "productos": [producto]
            }
            return nombre
    def mostrarCategorias(self):
        for clave, datos in categorias.items():
            print(f"IDCategoria: {clave} | Categoria: {datos['nombre'].nombre}")
            for datos2 in datos["productos"]:
                print(f"- {datos2}")