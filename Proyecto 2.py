from categorias import RegistroCategoria
from menus import Menu
from productos import RegistroProductos
menu = Menu()
categoria = RegistroCategoria()
producto = RegistroProductos(categoria)

while True:
    try:
        print(menu)
        op = int(input("Seleccione una opción: "))
        match op:
            case 1:
                producto.agregarProducto()
            case 2:
                categoria.agregarCategoria()
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                break
    except Exception as ex:
        print(f"Ha ocurrido un error: {ex}, vuelva a intentarlo")

