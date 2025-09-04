empleados = {}
class Empleados:
    def __init__(self, nombre, direccion, telefono, correo, puesto):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.puesto = puesto

    def __str__(self):
        return f"Nombre: {self.nombre} | Direccion: {self.direccion} | Telefono: {self.telefono} | Correo: {self.correo} | Puesto: {self.puesto}"

class GestionEmpleados:
    def agregarEmpleado(self, empleado, IDEmpleado):
        empleados[IDEmpleado] = empleado

    def mostrarEmpleados(self):
        for IDEmpleado, empleado in empleados.items():
            print(f"IDEmpleado: {IDEmpleado} | Empleado: {empleado}")
empleados[123] = Empleados("José","Mi casa",54563974,"Hola@gmail.com","JEFE")
empleados[321] = Empleados("Juan","Su casa",12345678,"Adios@gmail.com","Empleado")