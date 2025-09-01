from detallecompras import Detallecompras
from productos import Producto

class Compras:
    def __init__(self, fecha, total):
        self.fecha = fecha
        self.total = total

    def __str__(self):
        return f"Fecha: {self.fecha} | Total: {self.total}"

class RealizarCompra:
    def __init__(self):
        self.compra = {}

    def realizarlacompra(self,r):
        if r.categorias:
            print("Si")
        else:
            print("No")



