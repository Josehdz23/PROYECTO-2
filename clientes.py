class Clientes:
    def __init__(self,nombre, direccion, telefono, correo):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"Nombre: {self.nombre} | Direccion: {self.direccion} | Telefono: {self.telefono} | Correo: {self.correo}"

