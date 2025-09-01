from detallecompras import *
from productos import *
from categorias import *
import random
from datetime import datetime
detalle = DetallesCompras()
class Compras:
    def __init__(self, fecha, total):
        self.fecha = fecha
        self.total = total

    def __str__(self):
        return f"Fecha: {self.fecha} | Total: {self.total}"

class RealizarCompra:
    def __init__(self):
        self.compra = {}

    def realizarlacompra(self):
        while True:
            while True:
                IDCompra = random.randint(1,1000)
                if IDCompra not in self.compra.keys():
                    break
            fecha = datetime.now().date()
            agregardetalle = detalle.agregardetalle()
            total = 0
            if agregardetalle:
                for clave, datos in agregardetalle.items():
                    total = datos["detalle"].subtotal + total
                self.compra[IDCompra] = {
                    "Compra": Compras(fecha, total),
                    "Detalles": agregardetalle
                }
            for clave2, datos2 in self.compra.items():
                print("= = = = = TICKET DE COMPRA = = = = =")
            break








