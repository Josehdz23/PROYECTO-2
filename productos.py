class Producto:
    def __init__(self, nombre, precio, totalCompra, totalVenta, stock):
        self.nombre = nombre
        self.precio = precio
        self.totalCompra = totalCompra
        self.totalVenta = totalVenta
        self.stock = stock

    def __str__(self):
        self.stock = self.totalCompra - self.totalVenta
        return f"Nombre: {self.nombre} | Precio: {self.precio} | Stock: {self.stock}"

class RegistroProductos:
    def __init__(self):
        self.productos = {}

    def agregarProducto(self):
        while True:
            try:

            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")