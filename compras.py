from detallecompras import Detallecompras
from productos import Producto
from categorias import RegistroCategoria
p = Producto("COCA",1,3,"LASKD")
c = RegistroCategoria()
c.agregarCategoria(p)

class Compras:
    def __init__(self, fecha, total):
        self.fecha = fecha
        self.total = total

    def __str__(self):
        return f"Fecha: {self.fecha} | Total: {self.total}"

class RealizarCompra:
    def __init__(self):
        self.compra = {}

    def realizarlacompra(self,c):
        idCompra = 1234
        nombre = input("Ingrese el producto que desea realizar: ")
        precio = int(input("Ingrese el precio de la compra: "))
        fecha = input("Ingrese la fecha de la compra: ")
        cantidad = int(input("Ingrese la cantidad de productos: "))
        fechaCad = input("Ingrese la fecha de la caducidad producto: ")
        subtotal = precio * cantidad
        total = subtotal
        self.compra[idCompra] = {
            "Compra": Compras(fecha, total),
            "Detallecompra": Detallecompras(fechaCad, subtotal, cantidad,Producto(nombre,precio, 1,))
        }
        for c, d in self.compra.items():
            print(c,d["Detallecompra"],d["Producto"])




