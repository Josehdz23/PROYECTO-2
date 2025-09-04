from detallecompras import *
from empleados import *
from copy import deepcopy
import random
from datetime import datetime
detalle = DetallesCompras()
comprastotales = {}
class Compras:
    def __init__(self, fecha, total):
        self.fecha = fecha
        self.total = total

    def __str__(self):
        return f"Fecha: {self.fecha}\nTotal: {self.total}"

class RealizarCompra:
    def __init__(self):
        self.compra = {}

    def realizarlacompra(self, id):
        if empleados:
            if id not in empleados:
                print("No existe el empleado")
            else:
                if empleados[id].puesto == "JEFE":
                    while True:
                        while True:
                            IDCompra = random.randint(1, 1000)
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
                                "Empleado": empleados[id],
                                "IDEmpleado": id,
                                "Detalles": deepcopy(agregardetalle)
                            }
                            comprastotales[IDCompra] = {
                                "Compra": Compras(fecha, total),
                                "Empleado": empleados[id],
                                "IDEmpleado": id,
                                "Detalles": deepcopy(agregardetalle)
                            }
                        for clave2, datos2 in self.compra.items():
                            print("\n= = = = = TICKET DE COMPRA = = = = =")
                            print(f"ID Compra: {clave2}")
                            print(f"{datos2['Compra']}")
                            print(f"IDEmpleado: {datos2["IDEmpleado"]} {datos2['Empleado']}")
                            for idprod, detalledic in datos2["Detalles"].items():
                                print(f"-IDProducto:{idprod} {detalledic['producto']}")
                                print(f"-Detalles: {detalledic['detalle']}")
                                print(f"-Proveedor: {detalledic['proveedor']}")
                        detalle.detalles.clear()
                        self.compra.clear()
                        break
                elif empleados[id].puesto == "Empleado":
                    print("No tiene los permisos correspondientes para comprar productos para la tienda")
        else:
            print("No hay empleados, registrados")

    def mostrarComprasRealizadas(self):
        if comprastotales:
            for clave2, datos2 in comprastotales.items():
                print("\n= = = = = TICKET DE COMPRA = = = = =")
                print(f"ID Compra: {clave2}")
                print(f"{datos2['Compra']}")
                print(f"IDEmpleado: {datos2["IDEmpleado"]} {datos2['Empleado']}") # TERMINANDO DE DESPLEGAR
                for idprod, detalledic in datos2["Detalles"].items():
                    print(f"-IDProducto:{idprod} {detalledic['producto']}")
                    print(f"-Detalles: {detalledic['detalle']}")
                    print(f"-Proveedor: {detalledic['proveedor']}")
        else:
            print("No se ha realizado ninguna compra")