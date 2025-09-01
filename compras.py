from detallecompras import *
from productos import *
from categorias import *
import random
from datetime import datetime
detalles = DetallesCompras()
class Compras:
    def __init__(self, fecha, total):
        self.fecha = fecha
        self.total = total

    def __str__(self):
        return f"Fecha: {self.fecha} | Total: {self.total}"

class RealizarCompra:
    def __init__(self):
        self.compra = {}

    def realizarlacompra(self,compras):
        while True:
            while True:
                IDCompra = random.randint(1,1000)
                if IDCompra not in self.compra.keys():
                    break
            fecha = datetime.now().date()
            detalles.agregardetalle()








