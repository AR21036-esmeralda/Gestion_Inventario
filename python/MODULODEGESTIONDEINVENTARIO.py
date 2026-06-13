
# movimientos.py - Gestión de inventario con menú
from datetime import datetime
import os

# ========== FUNCIONES ==========
def registrar_entrada(inventario, movimientos, codigo, cantidad):
    """Registra una entrada de mercancía"""
    if codigo not in inventario:
        raise ValueError(f"El producto con código {codigo} no existe")
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser positiva")
    
    inventario[codigo]['stock'] += cantidad
    
    movimiento = {
        'fecha': datetime.now().isoformat(),
        'tipo': 'entrada',
        'codigo': codigo,
        'producto': inventario[codigo]['nombre'],
        'cantidad': cantidad
    }
    movimientos.append(movimiento)
    print(f"✓ Entrada registrada: +{cantidad} {inventario[codigo]['nombre']}")
    return movimiento


def registrar_salida(inventario, movimientos, codigo, cantidad):
    """Registra una salida de mercancía"""
    if codigo not in inventario:
        raise ValueError(f"El producto con código {codigo} no existe")
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser positiva")
    if inventario[codigo]['stock'] < cantidad:
        raise ValueError(f"Stock insuficiente. Stock actual: {inventario[codigo]['stock']}")
    
    inventario[codigo]['stock'] -= cantidad
    
    movimiento = {
        'fecha': datetime.now().isoformat(),
        'tipo': 'salida',
        'codigo': codigo,
        'producto': inventario[codigo]['nombre'],
        'cantidad': cantidad
    }
    movimientos.append(movimiento)
    print(f"✓ Salida registrada: -{cantidad} {inventario[codigo]['nombre']}")
    return movimiento


def agregar_producto(inventario, codigo, nombre, stock_inicial=0):
    """Agrega un nuevo producto al inventario"""
    if codigo in inventario:
        raise ValueError(f"El producto con código {codigo} ya existe")
    
    inventario[codigo] = {
        'nombre': nombre,
        'stock': stock_inicial
    }
    print(f"✓ Producto '{nombre}' agregado con stock: {stock_inicial}")
    return inventario[codigo]


def ver_stock(inventario):
    """Muestra el stock actual"""
    if not inventario:
        print(" No hay productos registrados")
        return
    
    print("\n" + "="*50)
    print("           STOCK ACTUAL")
    print("="*50)
    for codigo, datos in inventario.items():
        print(f"  {codigo} | {datos['nombre']} | Stock: {datos['stock']}")
    print("="*50)


def ver_movimientos(movimientos):
    """Muestra el historial"""
    if not movimientos:
        print(" No hay movimientos registrados")
        return
    
    print("\n" + "="*65)
    print("           HISTORIAL DE MOVIMIENTOS")
    print("="*65)
    for mov in movimientos:
        print(f"  {mov['fecha'][:19]} | {mov['tipo']:^6} | {mov['producto']} | ±{mov['cantidad']}")
    print("="*65)


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


# ========== MENU ==========
def menu():
    print("\n" + "="*40)
    print("   GESTIÓN DE MOVIMIENTOS DE INVENTARIO")
    print("="*40)
    print("  1. Agregar producto")
    print("  2. Registrar entrada")
    print("  3. Registrar salida")
    print("  4. Ver stock")
    print("  5. Ver movimientos")
    print("  6. Salir")
    print("="*40)


# ========== MAIN ==========
def main():
    inventario = {}
    movimientos = []
    
    # Productos de ejemplo
    agregar_producto(inventario, "001", "Laptop", 10)
    agregar_producto(inventario, "002", "Mouse", 20)
    agregar_producto(inventario, "003", "Teclado", 5)
    
    while True:
        menu()
        opcion = input("\nSeleccione opción (1-6): ").strip()
        
        if opcion == "1":
            limpiar_pantalla()
            print("\n--- AGREGAR PRODUCTO ---")
            codigo = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            try:
                stock = float(input("Stock inicial (0): ") or 0)
                agregar_producto(inventario, codigo, nombre, stock)
            except ValueError as e:
                print(f" Error: {e}")
            input("\nPresione Enter...")
            limpiar_pantalla()
            
        elif opcion == "2":
            limpiar_pantalla()
            print("\n--- REGISTRAR ENTRADA ---")
            codigo = input("Código del producto: ").strip()
            try:
                cantidad = float(input("Cantidad a ingresar: "))
                registrar_entrada(inventario, movimientos, codigo, cantidad)
            except ValueError as e:
                print(f" Error: {e}")
            input("\nPresione Enter...")
            limpiar_pantalla()
            
        elif opcion == "3":
            limpiar_pantalla()
            print("\n--- REGISTRAR SALIDA ---")
            codigo = input("Código del producto: ").strip()
            try:
                cantidad = float(input("Cantidad a retirar: "))
                registrar_salida(inventario, movimientos, codigo, cantidad)
            except ValueError as e:
                print(f"Error: {e}")
            input("\nPresione Enter...")
            limpiar_pantalla()
            
        elif opcion == "4":
            limpiar_pantalla()
            ver_stock(inventario)
            input("\nPresione Enter...")
            limpiar_pantalla()
            
        elif opcion == "5":
            limpiar_pantalla()
            ver_movimientos(movimientos)
            input("\nPresione Enter...")
            limpiar_pantalla()
            
        elif opcion == "6":
            limpiar_pantalla()
            print("\n¡Hasta luego!")
            break
            
        else:
            print("Opción inválida")
            input("\nPresione Enter...")
            limpiar_pantalla()


if __name__ == "__main__":
    main()
