from menus import *
from compras import *
from categorias import *
from productos import *
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
                    try:
                        idEmpleado = int(input("Ingresa el ID Empleado: "))
                        compra.realizarlacompra(idEmpleado)
                        break
                    except Exception as ex:
                        print(f"Ha ocurrido un error: {ex}")
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                prod.MostrarProducto()
            case 8:
                break
    except Exception as ex:
        print(f"Ha ocurrido un error: {ex}, vuelva a intentarlo")

