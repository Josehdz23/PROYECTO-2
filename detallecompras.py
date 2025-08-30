class Detallecompras:
    def __init__(self, fechaCaducidad, subtotal, cantidad):
        self.fechaCaducidad = fechaCaducidad
        self.subtotal = subtotal
        self.cantidad = cantidad

    def __str__(self):
        return f"Fecha de Caducidad: {self.fechaCaducidad} | Subtotal: {self.subtotal} | Cantidad: {self.cantidad}"