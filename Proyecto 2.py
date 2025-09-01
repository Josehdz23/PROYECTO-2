from menus import Menu
from compras import RealizarCompra
from categorias import RegistroCategoria
menu = Menu()
c = RegistroCategoria()
r = RealizarCompra()
r.realizarlacompra(c)

"""while True:
    try:
        print(menu)
        op = int(input("Seleccione una opción: "))
        match op:
            case 1:
                pass
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
                pass
            case 8:
                break
    except Exception as ex:
        print(f"Ha ocurrido un error: {ex}, vuelva a intentarlo")"""

