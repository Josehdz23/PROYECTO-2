class Producto:
    def __init__(self,nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.productos = {}

    def __str__(self):
        return f"Nombre: {self.nombre} | Precio: {self.precio} | Stock: {self.stock}"
