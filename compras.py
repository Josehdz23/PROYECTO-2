from detallecompras import Detallecompras
from productos import Producto
from categorias import RegistroCategoria

class Compras:
    def __init__(self, fecha, total):
        self.fecha = fecha
        self.total = total

    def __str__(self):
        return f"Fecha: {self.fecha} | Total: {self.total}"

class RealizarCompra:
    def __init__(self):
        self.compra = {}

    def realizarlacompra(self,aux):
        c = RegistroCategoria()
        idCompra = 1234
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        fecha = input("Ingrese la fecha de la compra: ")
        cantidad = int(input("Ingrese la cantidad de productos: "))
        fechaCad = input("Ingrese la fecha de la caducidad producto: ")
        c.agregarCategoria(Producto(nombre,precio, 1,))
        subtotal = precio * cantidad
        total = subtotal
        self.compra[idCompra] = {
            "Compra": Compras(fecha, total),
            "Detallecompra": Detallecompras(fechaCad, subtotal, cantidad,Producto(nombre,precio, 1,))
        }
        for c, d in self.compra.items():
            print(c,d["Detallecompra"])




