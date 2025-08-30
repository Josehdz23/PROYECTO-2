class Empleados:
    def __init__(self, nombre, direccion, telefono, correo, puesto):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.puesto = puesto

    def __str__(self):
        return f"Nombre: {self.nombre} | Direccion: {self.direccion} | Telefono: {self.telefono} | Correo: {self.correo} | Puesto: {self.puesto}"