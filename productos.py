class Producto:
    def __init__(self,IDProducto, nombre, precio, stock):
        self.IDProducto = IDProducto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        self.stock = self.totalCompra - self.totalVenta
        return f"Nombre: {self.nombre} | Precio: {self.precio} | Stock: {self.stock}"

class RegistroProductos:
    def __init__(self, registro):
        self.productos = {}
        self.registro = registro

    def agregarProducto(self):
        if self.registro.categorias:
            while True:
                try:
                    id = int(input("Ingrese el ID del producto: "))
                    if id in self.productos:
                except Exception as ex:
                    print(f"Ha ocurrido un error: {ex}")
        else:
            print("Debe haber una categoría creada para poder ingresar un producto!! ")