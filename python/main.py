from MODULO_GESTION_PRODUCTOS import menu_productos
from MODULO_GESTION_PROVEEDORES import menu_proveedores
from MODULO_MOVIMIENTOS_INVENTARIO import menu_movimientos

inventario = {}
proveedores = {}
movimientos = []

while True:

    print("\n" + "=" * 40)
    print("   SISTEMA DE INVENTARIO")
    print("=" * 40)

    print("1. Gestion de proveedores")
    print("2. Gestion de productos")
    print("3. Movimientos de inventario")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    match opcion:

        case "1":
            menu_proveedores(proveedores)

        case "2":
            menu_productos(
                inventario,
                proveedores
            )

        case "3":
             menu_movimientos(
                 inventario,
                   movimientos
            )    

        case "4":
            print("Saliendo del sistema...")
            break

        case _:
            print("Opcion invalida")



            