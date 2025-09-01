categorias = {}
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Nombre Categoria: {self.nombre}"


class RegistroCategoria:
    def agregarCategoria(self,id,producto,cantidad):
        if id in categorias:
            for obj in categorias[id]["productos"]:
                if obj.nombre == producto.nombre:
                    obj.stock += cantidad
                    return categorias[id]["nombre"].nombre
        else:
            nombre = input("La categoria no existía pero se creará, ingrese el nombre del categoría: ")
            categorias[id] = {
                "nombre": Categoria(nombre),
                "productos": [producto]
            }
            return nombre
    def mostrarCategorias(self):
        for clave, datos in categorias.items():
            print(f"IDCategoria: {clave}")
            for datos2 in datos["productos"]:
                print(f"- {datos2}")

