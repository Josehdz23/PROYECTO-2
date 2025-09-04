from menus import *
from compras import *
from categorias import *
from productos import *
from proveedores import *
from empleados import *
emp = GestionEmpleados()
prov = GestionProveedores()
menu = Menu()
prod = GestionProductos()
categoria = RegistroCategoria()
compra = RealizarCompra()

while True:
    try:
        print(menu)
        op = int(input("Seleccione una opción: "))
        match op:
            case 1:
                while True:
                    idEmpleado = int(input("Ingresa el ID Empleado: "))
                    if idEmpleado > 0:
                        compra.realizarlacompra(idEmpleado)
                    break
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                categoria.mostrarCategorias()
            case 7:
                prod.MostrarProducto()
            case 8:
                pass
            case 9:
                prov.mostrarProveedores()
            case 10:
                pass
            case 11:
                compra.mostrarComprasRealizadas()
            case 12:
                pass
            case 13:
                pass
            case 14:
                emp.mostrarEmpleados()
            case _:
                print("Esa opción no existe, reintente")
    except Exception as ex:
        print(f"Ha ocurrido un error: {ex}, vuelva a intentarlo")