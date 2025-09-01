from productos import *
from datetime import datetime
from categorias import *
import random

class Detalles:
    def __init__(self, fechaCaducidad, subtotal, cantidad):
        self.fechaCaducidad = fechaCaducidad
        self.subtotal = subtotal
        self.cantidad = cantidad

    def __str__(self):
        return f"Fecha de Caducidad: {self.fechaCaducidad} | Subtotal: {self.subtotal} | Cantidad: {self.cantidad}"

class DetallesCompras:
    def __init__(self):
        self.detalles = {}

    def agregardetalle(self):
        while True:
            try:
                idProducto = int(input("Ingrese el ID del producto: "))
                if idProducto in productos:
                    while True:
                        fechaCaducidad = input("Ingresa la fecha de caducidad del producto (dd-mm-yyyy): ")
                        try:
                            fecha_valida = datetime.strptime(fechaCaducidad, "%d-%m-%Y").date()
                            break
                        except Exception as ex:
                            print(f"Ha ocurrido un error: {ex}")
                    while True:
                        try:
                            cantidad = int(input("Ingrese la cantidad de productos a comprar: "))
                            if cantidad > 0:
                                break
                            else:
                                print("La cantidad no es válida, reintente")
                        except Exception as ex:
                            print(f"Ha ocurrido un error: {ex}")
                    subtotal = cantidad * productos[idProducto].precio
                    productos[idProducto].stock += cantidad
                    self.detalles[idProducto] = {
                        "producto": productos[idProducto],
                        "detalle": Detalles(fecha_valida, subtotal, cantidad)
                    }
                else:
                    decision = input("El producto no existe, ¿Desea agregarlo como nuevo? (Si/No): ").lower()
                    if decision == "si":
                        while True:
                            nombreProducto = input("Ingrese el nombre del producto: ")
                            if nombreProducto.strip() == "":
                                print("El nombre no es válido, reintente")
                            else:
                                if nombreProducto in productos:
                                    print("El nombre del producto ya existe, reintente")
                                else:
                                    break
                        while True:
                            try:
                                precio = float(input("Ingrese el precio del producto: "))
                                if precio > 0:
                                    break
                                else:
                                    print("El precio no es válido, reintente")
                            except Exception as ex:
                                print(f"Ha ocurrido un error: {ex}")
                        while True:
                            fechaCaducidad = input("Ingresa la fecha de caducidad del producto (dd-mm-yyyy): ")
                            try:
                                fecha_valida = datetime.strptime(fechaCaducidad, "%d-%m-%Y").date()
                                break
                            except Exception as ex:
                                print(f"Ha ocurrido un error: {ex}")
                        while True:
                            try:
                                cantidad = int(input("Ingrese la cantidad de productos a comprar: "))
                                if cantidad > 0:
                                    break
                                else:
                                    print("La cantidad no es válida, reintente")
                            except Exception as ex:
                                print(f"Ha ocurrido un error: {ex}")
                        stock = cantidad
                        while True:
                            try:
                                cat = RegistroCategoria()
                                codcat = int(input("Ingrese el codigo de la categoria: "))
                                p = Producto(nombreProducto, precio, stock, "s")
                                nombrecat = cat.agregarCategoria(codcat, p, cantidad)
                                break
                            except Exception as ex:
                                print(f"Ha ocurrido un error: {ex}")
                        nuevo = Producto(nombreProducto, precio, stock, nombrecat)
                        subtotal = cantidad * precio
                        gestion = GestionProductos()
                        gestion.agregarProducto(nuevo, idProducto)
                        self.detalles[idProducto] = {
                            "producto": nuevo,
                            "detalle": Detalles(fecha_valida, subtotal, cantidad)
                        }
                continuar = input("¿Desea continuar? (Si/No): ").lower()
                if continuar == "no":
                    break
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")
        return self.detalles




