Algoritmo MODULO_GESTION_DE_PRODUCTOS
		
	Definir nombres Como Caracter
	Definir precios Como Real
	Definir stocks,contador,eleccion,limite,codigo,modificar, i,m Como Entero
	contador <- 1
	limite <- 100
	
	
	//creamos los arrays
	Dimension codigo[limite]
	Dimension nombres[limite]
	Dimension precios[limite]
	Dimension stocks[limite]
	
	// Menu de inicio
	Repetir
		Escribir "Seleccione 1, 2, 3, 4 según la acción que desea realizar"
		Escribir"-------------------------------------------------"
		Escribir "--------MENU PRINCIPAL-------" 
		Escribir"1.Crear producto"
		Escribir"2.Mostrar Productos"
		Escribir"3.Modificar informacion de producto"
		Escribir"4.Salir"
		Leer eleccion 
		
		Segun eleccion Hacer
			1: 
				Si contador < limite Entonces
					Escribir"Ingrese el codigo del producto"
					Leer codigo[contador]
					Escribir " Ingrese el nombre del producto"
					Leer nombres[contador]
					Escribir " Ingrese el precio unitario del producto"
					Leer precios[contador]
					Escribir " Ingrese la cantidad de stock de ese producto en bodega"
					Leer stocks[contador]
					contador <- contador+1

					
				SiNo
					Escribir "No hay espacio para más productos"
				Fin Si
			2:
			    Si contador = 1 Entonces 
					Escribir " No hay productos por mostrar"
				SiNo
					Para i<-1 Hasta contador-1 Hacer
						Escribir i, " - Codigo: ", codigo[i], " | Producto: ", nombres[i], " | Precio: ", precios[i], " | Stock: ", stocks[i]			
						
					FinPara
				FinSi
				
		    3:	
				Escribir " Ingrese el codigo del producto que desea modificar"
				
				Leer modificar
				
				Para m<-1 Hasta contador-1 Hacer
					si modificar = codigo[m] Entonces
						Escribir" Ingrese la nueva cantidad del stock del producto"
						Leer stocks[m]
						
						Escribir" Ingrese el nuevo precio del producto"
						Leer precios[m]
						
						Escribir "-------------- Datos Modificados con exito----------"
						Escribir m, "- Codigo: ", codigo[m]	, " | Producto: ", nombres[m], " | Precio: ", precios[m], " | Stock: ", stocks[m]
					SiNo
						Escribir" Codigo no encontrado"
						
						
					FinSi
					
				FinPara
		FinSegun
		
		
		
		
	Hasta Que eleccion = 4  
	
FinAlgoritmo
