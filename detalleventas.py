class Detalleventas:
    def __init__(self, cantidad, subtotal, stock):
        self.cantidad = cantidad
        self.subtotal = subtotal
        self.stock = stock

    def __str__(self):
        return f"Cantidad: {self.cantidad} | Subtotal: {self.subtotal} | Stock: {self.stock}"