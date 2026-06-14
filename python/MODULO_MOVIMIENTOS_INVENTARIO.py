

from MODULO_GESTION_PRODUCTOS import validar_numero_entero_positivo
from MODULO_GESTION_PROVEEDORES import validar_codigo
from datetime import datetime

def registrar_entrada(inventario, movimientos, codigo, cantidad, motivo, proveedor=None):
    """Registra una entrada de mercancía"""
    if codigo not in inventario:
        raise ValueError(f"El producto con codigo {codigo} no existe")
    
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser positiva")
    
    inventario[codigo]['stock'] += cantidad
    
    movimiento = {
        'fecha': datetime.now().isoformat(),
        'tipo': 'entrada',
        'codigo': codigo,
        'producto': inventario[codigo]['nombre'],
        'cantidad': cantidad,
        'motivo': motivo,
        'proveedor': proveedor if motivo == 'compra' else None,
        'stock_resultante': inventario[codigo]['stock']
    }
    movimientos.append(movimiento)
    print(f"[OK] Entrada registrada. Nuevo stock de {inventario[codigo]['nombre']}: {inventario[codigo]['stock']}")


def registrar_salida(inventario, movimientos, codigo, cantidad, motivo, destino=None):
    """Registra una salida de mercancía"""
    if codigo not in inventario:
        raise ValueError(f"El producto con codigo {codigo} no existe")
    
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser positiva")
    
    if inventario[codigo]['stock'] < cantidad:
        raise ValueError(f"Stock insuficiente. Disponible: {inventario[codigo]['stock']}")
    
    inventario[codigo]['stock'] -= cantidad
    
    movimiento = {
        'fecha': datetime.now().isoformat(),
        'tipo': 'salida',
        'codigo': codigo,
        'producto': inventario[codigo]['nombre'],
        'cantidad': cantidad,
        'motivo': motivo,
        'destino': destino if motivo == 'venta' else None,
        'stock_resultante': inventario[codigo]['stock']
    }
    movimientos.append(movimiento)
    print(f"[OK] Salida registrada. Nuevo stock de {inventario[codigo]['nombre']}: {inventario[codigo]['stock']}")


def consultar_stock(inventario, codigo=None):
    """Consulta stock de un producto o de todos"""
    if codigo:
        if codigo not in inventario:
            print(f"[ERROR] Producto {codigo} no encontrado")
            return
        prod = inventario[codigo]
        print(f"\n[PRODUCTO] {prod['nombre']} (Codigo: {codigo})")
        print(f"   Stock: {prod['stock']} | Precio: ${prod.get('precio', 0)}")
    else:
        print("\n[LISTA COMPLETA DE PRODUCTOS]")
        print("-" * 50)
        for cod, prod in inventario.items():
            print(f"{cod} | {prod['nombre']:20} | Stock: {prod['stock']:4} | ${prod.get('precio', 0)}")
        print("-" * 50)


def ver_movimientos(movimientos, filtro=None):
    """Muestra el historial de movimientos"""
    if not movimientos:
        print("\n[INFO] No hay movimientos registrados")
        return
    
    if filtro:
        movimientos_filtrados = [m for m in movimientos if m['codigo'] == filtro]
        if not movimientos_filtrados:
            print(f"\n[ERROR] No hay movimientos para el producto {filtro}")
            return
        mostrar = movimientos_filtrados
        print(f"\n[MOVIMIENTOS DEL PRODUCTO {filtro}]")
    else:
        mostrar = movimientos
        print("\n[HISTORIAL COMPLETO DE MOVIMIENTOS]")
    
    print("=" * 90)
    for m in mostrar:
        print(f"{m['fecha'][:19]} | {m['tipo'].upper():6} | "
              f"{m['codigo']} - {m['producto'][:20]:20} | "
              f"Cant: {m['cantidad']:4} | Motivo: {m['motivo']:15} | "
              f"Stock final: {m['stock_resultante']}")
    print("=" * 90)


def stock_valorizado(inventario):
    """Calcula el valor total del inventario"""
    total = 0
    for datos in inventario.values():
        total += datos['stock'] * datos.get('precio', 0)
    return total


def mostrar_resumen(inventario, movimientos):
    """Muestra un resumen general"""
    print("\n" + "=" * 50)
    print("[RESUMEN DE INVENTARIO]")
    print("=" * 50)
    print(f"Total de productos: {len(inventario)}")
    print(f"Total de movimientos: {len(movimientos)}")
    
    entradas = len([m for m in movimientos if m['tipo'] == 'entrada'])
    salidas = len([m for m in movimientos if m['tipo'] == 'salida'])
    print(f"Entradas: {entradas} | Salidas: {salidas}")
    
    valor_total = stock_valorizado(inventario)
    print(f"Valor total del inventario: ${valor_total:.2f}")
    
    # Productos con bajo stock (menos de 5)
    bajo_stock = [(cod, d['nombre'], d['stock']) for cod, d in inventario.items() if d['stock'] < 5]
    if bajo_stock:
        print("\n[ALERTA] PRODUCTOS CON BAJO STOCK (<5 unidades):")
        for cod, nombre, stock in bajo_stock:
            print(f"   {cod} - {nombre}: {stock} unidades")
    print("=" * 50)


# ========== FUNCION MENU ==========

def menu_movimientos(inventario, movimientos):
   
    while True:
        print("\n" + "=" * 50)
        print("SISTEMA DE MOVIMIENTOS DE INVENTARIO")
        print("=" * 50)
        print("1. Registrar ENTRADA de mercancia")
        print("2. Registrar SALIDA de mercancia")
        print("3. Consultar stock de un producto")
        print("4. Ver listado completo de productos")
        print("5. Ver historial de movimientos")
        print("6. Ver movimientos de un producto especifico")
        print("7. Ver resumen general")
        print("8. Salir del menu de movimientos")
        print("=" * 50)
        
        opcion = input("\nSeleccione una opcion: ").strip()
        
        # Opcion 1: Registrar entrada
        if opcion == "1":
            print("\n--- REGISTRAR ENTRADA ---")
            codigo = validar_codigo("Codigo del producto: ")
            if codigo not in inventario:
                print(f"[ERROR] Producto {codigo} no existe. Registrelo primero en productos.")
                continue
            
            try:
                cantidad = validar_numero_entero_positivo("Cantidad: ")
                print("Motivos disponibles: compra, devolucion_cliente, ajuste")
                motivo = input("Motivo: ").strip().lower()
                if motivo not in ['compra', 'devolucion_cliente', 'ajuste']:
                    print("[ERROR] Motivo no valido. Usando 'ajuste' por defecto")
                    motivo = 'ajuste'
                
                proveedor = None
                if motivo == 'compra':
                    proveedor = input("Proveedor (opcional): ").strip() or None
                
                registrar_entrada(inventario, movimientos, codigo, cantidad, motivo, proveedor)
            except ValueError as e:
                print(f"[ERROR] {e}")
        
        # Opcion 2: Registrar salida
        elif opcion == "2":
            print("\n--- REGISTRAR SALIDA ---")
            codigo = validar_codigo("Codigo del producto: ")
            if codigo not in inventario:
                print(f"[ERROR] Producto {codigo} no existe")
                continue
            
            try:
                cantidad = validar_numero_entero_positivo("Cantidad: ")
                print("Motivos disponibles: venta, devolucion_proveedor, merma, ajuste")
                motivo = input("Motivo: ").strip().lower()
                if motivo not in ['venta', 'devolucion_proveedor', 'merma', 'ajuste']:
                    print("[ERROR] Motivo no valido. Usando 'venta' por defecto")
                    motivo = 'venta'
                
                destino = None
                if motivo == 'venta':
                    destino = input("Destino/cliente (opcional): ").strip() or None
                
                registrar_salida(inventario, movimientos, codigo, cantidad, motivo, destino)
            except ValueError as e:
                print(f"[ERROR] {e}")
        
        # Opcion 3: Consultar stock de un producto
        elif opcion == "3":
            codigo = validar_codigo("\nCodigo del producto: ")
            consultar_stock(inventario, codigo)
        
        # Opcion 4: Ver listado completo
        elif opcion == "4":
            consultar_stock(inventario)
        
        # Opcion 5: Ver historial completo
        elif opcion == "5":
            ver_movimientos(movimientos)
        
        # Opcion 6: Ver movimientos de un producto
        elif opcion == "6":
            codigo = validar_codigo("\nCodigo del producto: ")
            ver_movimientos(movimientos, codigo)
        
        # Opcion 7: Resumen general
        elif opcion == "7":
            mostrar_resumen(inventario, movimientos)
        
        # Opcion 8: Salir
        elif opcion == "8":
            print("\n[SALIDA] Saliendo del menu de movimientos...")
            break
        
        else:
            print("[ERROR] Opcion no valida. Intente de nuevo.")
        
        input("\nPresione Enter para continuar...")




if __name__ == "__main__":
    
    inventario = {
        'PR001': {'nombre': 'Laptop Gamer', 'stock': 10, 'precio': 850.00},
        'PR002': {'nombre': 'Mouse RGB', 'stock': 50, 'precio': 25.50},
        'PR003': {'nombre': 'Teclado Mecanico', 'stock': 15, 'precio': 65.00},
        'PR004': {'nombre': 'Monitor 24"', 'stock': 5, 'precio': 180.00},
    }
    
    movimientos = []  # Lista para el historial
    
    # Iniciar el menu
    menu_movimientos(inventario, movimientos)
    