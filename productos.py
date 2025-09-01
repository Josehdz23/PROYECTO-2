class Producto:
    def __init__(self,IDProducto,nombre, precio, stock):
        self.nombre = nombre
        self.IDProducto = IDProducto
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"IDProducto: {self.IDProducto} | Nombre: {self.nombre} | Precio: {self.precio} | Stock: {self.stock}"
