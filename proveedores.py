import random
proveedores = {}
class Proveedores:
    def __init__(self, nombre, direccion, telefono, correo, empresa):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.empresa = empresa

    def __str__(self):
        return f"Nombre: {self.nombre} | Direccion: {self.direccion} | Telefono: {self.telefono} | Correo: {self.correo} | Empresa: {self.empresa}"

class GestionProveedores:
    def agregarProveedor(self, proveedor):
        idProv = random.randint(2000, 3000)
        if proveedor not in proveedores:
            proveedores[idProv] = proveedor

    def mostrarProveedores(self):
        for clave, datos in proveedores.items():
            print(clave, datos)