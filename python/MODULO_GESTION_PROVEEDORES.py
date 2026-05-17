def validar_texto_no_vacio(mensaje):

    while True:

        texto = input(mensaje).strip()

        if texto == "":
            print("Error: no puede estar vacio")
        else:
            return texto



def registrar_proveedor(proveedores):

    codigo_proveedor = validar_texto_no_vacio("Ingrese codigo del proveedor: ")
    if codigo_proveedor in proveedores:
        print ("Error : Ya existe un proveedor con ese codigo " )
        return 
    
    nombre_proveedor= validar_texto_no_vacio("Ingrese el nombre del proveedor: ")
       
    telefono_proveedor= validar_texto_no_vacio("Ingrese el telefono del proveedor: ") 
    
    direccion_proveedor= validar_texto_no_vacio("Ingrese la  direccion del proveedor: ") 
     
    
# Guarda un proveedor dentro del diccionario proveedores usando el codigo como clave
    
    proveedores[codigo_proveedor]={
       "nombre": nombre_proveedor,
       "telefono": telefono_proveedor,
       "direccion": direccion_proveedor
    } 

    print ("---------Proveedor Registrado con Exito  ------")


def mostrar_proveedores(proveedores):
    
    if proveedores=={}:
        print("---------No hay proveedores por mostrar---------")
        return
    
    print("\n" + "=" * 40)
    print("       LISTA DE PROVEEDORES")
    print("=" * 40)

    for codigo_proveedor,datos in proveedores.items():
       
       print("codigo_proveedor:",codigo_proveedor)

       for clave,valor in datos.items():
           print(clave,":" ,valor)

       print("-" * 40)        



def buscar_proveedor(proveedores):      
    codigo_proveedor=input("Ingrese el codigo del proveedor que desea buscar: ")
    proveedor = proveedores.get(codigo_proveedor)

    if proveedor:
        print("---------proveedor encontrado---------")
        print(proveedor)
    else:
        print("---------proveedor no encontrado---------")



def editar_informacion_proveedor(proveedores):
    
    codigo_proveedor= input("Ingrese el codigo del proveedor que desea modificar: ")

    if codigo_proveedor in proveedores:
         print("¿Qué desea modificar?")
         print("1.Modificar telefono ")
         print("2.Modificar direccion ")
         print("3.Modificar direccion y telefono")
         opcion = input("Ingrese opcion: ")

         match opcion :
             case "1" :
                 nuevo_numero_telefono = validar_texto_no_vacio("Nuevo telefono: ")
                 proveedores[codigo_proveedor]["telefono"] = nuevo_numero_telefono
                 print("---telefono actualizado con exito---")

             case "2":
                 nueva_direccion=validar_texto_no_vacio("Nueva direccion: ")
                 proveedores[codigo_proveedor]["direccion"] = nueva_direccion  
                 print("-----direccion actualizada con exito-----")

             case "3":
                 nuevo_numero_telefono = validar_texto_no_vacio("Nuevo telefono: ") 
                 nueva_direccion = validar_texto_no_vacio ("Nueva direccion: ")  

                 proveedores[codigo_proveedor]["telefono"] = nuevo_numero_telefono
                 proveedores[codigo_proveedor]["direccion"]= nueva_direccion
                 print("----proveedor actualizado con exito-------")
            
             case _ :
                 print("opcion invalida")

    else:
        print("proveedor no encontrado")



def eliminar_proveedor(proveedores):
    print("eliminar proveedor")
    codigo_proveedor=input("Ingrese el codigo del proveedor que desea eliminar: ")
    if codigo_proveedor in proveedores:
        del proveedores[codigo_proveedor]
        print("---------proveedor eliminado con exito---------")
    else:
        print("proveedor no encontrado")    
        




# funcion mostrar menu 
def mostrar_menu_proveedores():
    print("\n" + "=" * 40)
    print("  GESTION DE PROVEEDORES")
    print("=" * 40)
    print("1.Registrar proveedor")
    print("2.Mostrar proveedores")
    print("3.Buscar proveedor ")
    print("4.Editar informacion de proveedor")
    print("5.Borrar proveedor")
    print("6.salir")
    print("=" * 40)



def menu_proveedores(proveedores):
    
  while True:

    mostrar_menu_proveedores()
    opcion= input("seleccione una opcion: ")

    match opcion:
        case "1":
            registrar_proveedor(proveedores)

        case "2":
            mostrar_proveedores(proveedores)

        case "3":
            buscar_proveedor(proveedores)

        case "4":
            editar_informacion_proveedor(proveedores)

        case "5":
            eliminar_proveedor(proveedores)

        case "6":
            print("Saliendo del modulo de proveedores...")
            break

        case _:
            print("Opcion invalida")


# Bloque de prueba individual del modulo de proveedores

if __name__ == "__main__":

    proveedores = {}

    menu_proveedores(proveedores)




     