
Algoritmo MODULO_GESTION_DE_PROVEEDORES
	
	Definir nombres Como Caracter
	Definir telefonos Como Caracter
	Definir direcciones Como Caracter
	Definir contador, eleccion, limite, codigo, modificar, i, m Como Entero
	
	contador <- 1
	limite <- 100
	
	
	// Creamos los arrays
	Dimension codigo[limite]
	Dimension nombres[limite]
	Dimension telefonos[limite]
	Dimension direcciones[limite]
	
	
	// Menu de inicio
	Repetir
		Escribir "Seleccione 1, 2, 3, 4 según la acción que desea realizar"
		Escribir "-------------------------------------------------"
		Escribir "--------MENU PRINCIPAL-------"
		Escribir "1. Crear proveedor"
		Escribir "2. Mostrar proveedores"
		Escribir "3. Modificar informacion de proveedor"
		Escribir "4. Salir"
		
		Leer eleccion
		
		Segun eleccion Hacer
			
			1:
				Si contador < limite Entonces
					
					Escribir "Ingrese el codigo del proveedor"
					Leer codigo[contador]
					
					Escribir "Ingrese el nombre del proveedor"
					Leer nombres[contador]
					
					Escribir "Ingrese el telefono del proveedor"
					Leer telefonos[contador]
					
					Escribir "Ingrese la direccion del proveedor"
					Leer direcciones[contador]
					
					contador <- contador + 1
					
				SiNo
					Escribir "No hay espacio para más proveedores"
				FinSi
				
				
			2:
				Si contador = 1 Entonces
					Escribir "No hay proveedores por mostrar"
				SiNo
					
					Para i <- 1 Hasta contador - 1 Hacer
						
					Escribir i, " - Codigo: ", codigo[i], " | Proveedor: ", nombres[i], " | Telefono: ", telefonos[i], " | Direccion: ", direcciones[i] 
					FinPara
					
				FinSi
				
				
			3:
				Escribir "Ingrese el codigo del proveedor que desea modificar"
				Leer modificar
				
				Para m <- 1 Hasta contador - 1 Hacer
					
					Si modificar = codigo[m] Entonces
						
						Escribir "Ingrese el nuevo telefono del proveedor"
						Leer telefonos[m]
						
						Escribir "Ingrese la nueva direccion del proveedor"
						Leer direcciones[m]
						
						Escribir "-------------- Datos Modificados con exito ----------"
						
						Escribir m, " - Codigo: ", codigo[m], " | Proveedor: ", nombres[m], " | Telefono: ", telefonos[m], " | Direccion: ", direcciones[m]
						
					SiNo
						Escribir "Codigo no encontrado"
						
					FinSi
					
				FinPara
				
		FinSegun
		
		
	Hasta Que eleccion = 4
	
FinAlgoritmo