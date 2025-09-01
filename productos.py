productos = {}
class Producto:
    def __init__(self,nombre, precio, stock, categoria):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def __str__(self):
        return f"Nombre: {self.nombre} | Precio: {self.precio} | Stock: {self.stock} | Categoria: {self.categoria}"

class GestionProductos:
    def agregarProducto(self, producto, IDProducto):
        productos[IDProducto] = producto

    def MostrarProducto(self):
        if productos:
            for clave, datos in productos.items():
                print(clave, datos)
        else:
            print("No productos")