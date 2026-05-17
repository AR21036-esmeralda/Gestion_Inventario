def validar_numero_entero_positivo(mensaje):
       while True:
          try:
             valor= int(input(mensaje))
             if valor< 0:
                print("Error: no puede ser negativo")
             else:
                return valor
          except:
             print("Error: debe ingresar un numero valido" )


def validar_numero_decimal_positivo(mensaje):
       while True:
          try:
             valor= float(input(mensaje))
             if valor< 0:
                print("Error: no puede ser negativo")
             else:
                return valor
          except:
             print("Error: debe ingresar un numero valido" )                   




def ingresar_producto(inventario,proveedores):

    codigo = input("Ingrese codigo del producto: ")
    if codigo in inventario:
        print ("Error : Ya existe un producto con ese codigo " )
        return 
    
    nombre= input("Ingrese el nombre del producto: ")
       
    precio= validar_numero_decimal_positivo("Ingrese el precio del producto: ") 
    
    stock= validar_numero_entero_positivo("Ingrese la cantidad de producto en bodega: ") 

    codigo_proveedor = input(
    "Ingrese codigo del proveedor: "
)

    if codigo_proveedor not in proveedores:
     print("Error: el proveedor no existe. Debe registrarlo antes de asignarlo al producto")
     return 

     
    
      #Guarda un producto dentro del diccionario inventario usando el código como clave”

    inventario[codigo]={
       "nombre": nombre,
       "precio": precio,
       "stock": stock,
       "proveedor": codigo_proveedor
    } 

    print ("---------Producto Ingresado con Exito  ------")





def mostrar_productos(inventario):
    
    if inventario=={}:
        print("---------No hay productos por mostrar---------")
        return
    
    print("\n" + "=" * 40)
    print("       LISTA DE PRODUCTOS")
    print("=" * 40)

    for codigo,datos in inventario.items():
       
       print("codigo_producto:",codigo)

       for clave,valor in datos.items():
           print(clave,":" ,valor)

       print("-" * 40)    
           

def buscar_producto(inventario):      
    codigo=input("Ingrese el codigo del producto que desea buscar: ")
    producto= inventario.get(codigo)

    if producto:
        print("---------producto encontrado---------")
        print(producto)
    else:
        print("---------producto no encontrado---------")



def editar_informacion_producto(inventario):
    
    codigo= input("Ingrese el codigo del producto que desea modificar: ")

    if codigo in inventario:
         print("¿Qué desea modificar?")
         print("1.Modificar Precio ")
         print("2.Modificar stock ")
         print("3.Modificar precio y stock ")
         opcion = input("Ingrese opcion: ")

         match opcion :
             case "1" :
                 nuevo_precio = validar_numero_decimal_positivo("Nuevo precio: ")
                 inventario[codigo]["precio"] = nuevo_precio
                 print("---precio actualizado con exito---")

             case "2":
                 nuevo_stock=validar_numero_entero_positivo ("Nuevo stock: ")
                 inventario[codigo]["stock"] = nuevo_stock  
                 print("-----stock actualizado con exito-----")

             case "3":
                 nuevo_precio = validar_numero_decimal_positivo("Nuevo precio: ") 
                 nuevo_stock = validar_numero_entero_positivo ("Nuevo stock: ")  

                 inventario[codigo]["precio"] = nuevo_precio
                 inventario[codigo]["stock"]= nuevo_stock
                 print("----producto actualizado con exito-------")
            
             case _ :
                 print("opcion invalida")

    else:
        print("producto no encontrado")



def eliminar_producto(inventario):
    print("eliminar producto")
    codigo=input("Ingrese el codigo del producto que desea eliminar: ")
    if codigo in inventario:
        del inventario[codigo]
        print("---------producto eliminado con exito---------")
    else:
        print("producto no encontrado")    
        




# funcion mostrar menu 
def mostrar_menu():
    print("\n" + "=" * 40)
    print("  GESTION DE PRODUCTOS")
    print("=" * 40)
    print("1.Ingresar producto")
    print("2.Mostrar productos")
    print("3.Buscar producto ")
    print("4.Editar informacion de producto")
    print("5.Borrar producto")
    print("6.salir")
    print("=" * 40)

def menu_productos(inventario, proveedores):

    
    while True:
        mostrar_menu()
        opcion= input("seleccione una opcion: ")

        match opcion:
            case "1":
             ingresar_producto(inventario,proveedores)
        

            case "2":
              mostrar_productos(inventario)

            case "3":
              buscar_producto(inventario)  

            case"4"  : 
              editar_informacion_producto(inventario)   

            case"5":
              eliminar_producto(inventario)
                
        
            case "6":
              print("saliendo del modulo gestion productos...")
              break

            case _:
                print("Opcion invalida")
   

# Datos de prueba para ejecutar el modulo

if __name__ == "__main__":

    inventario = {}

    proveedores = {

        "PR001": {
            "nombre": "TechSupply",
            "telefono": "7777-7777",
            "direccion": "San Salvador"
        },

        "PR002": {
            "nombre": "OfficeMarket",
            "telefono": "8888-8888",
            "direccion": "Santa Ana"
        }

    }

    menu_productos(
        inventario,
        proveedores
    )     