Algoritmo Sistema_Gestion_Inventario_Grupo1
	Definir opcion_principal Como Entero
	
	Repetir
		Limpiar Pantalla
		Escribir "================================================="
		Escribir "   SISTEMA INTEGRADO DE INVENTARIO - GRUPO 1"
		Escribir "================================================="
		Escribir "1. Modulo de Gestion de Productos (Esmeralda)"
		Escribir "2. Modulo de Movimientos de Inventario (Cesar)"
		Escribir "3. Salir del Sistema"
		Escribir "-------------------------------------------------"
		Escribir "Seleccione una opcion: "
		Leer opcion_principal
		
		Segun opcion_principal Hacer
			1:
				Modulo_Esmeralda_Gestion
			2:
				Modulo_Cesar_Movimientos
			3:
				Escribir "Cerrando sistema... ¡Exitos en la defensa!"
			De Otro Modo:
				Escribir "Opcion no valida."
				Esperar 2 Segundos
		Fin Segun
	Hasta Que opcion_principal = 3
FinAlgoritmo

SubProceso Modulo_Esmeralda_Gestion
	Definir nombres Como Caracter
	Definir precios Como Real
	Definir stocks,contador,eleccion,limite,codigo,modificar, i,m Como Entero
	contador <- 1
	limite <- 100
	
	Dimension codigo[limite]
	Dimension nombres[limite]
	Dimension precios[limite]
	Dimension stocks[limite]
	
	Repetir
		Limpiar Pantalla
		Escribir "--------MODULO GESTION DE PRODUCTOS-------" 
		Escribir "1. Crear producto"
		Escribir "2. Mostrar Productos"
		Escribir "3. Modificar informacion de producto"
		Escribir "4. Regresar al Menu Principal"
		Escribir "------------------------------------------"
		Leer eleccion 
		
		Segun eleccion Hacer
			1: 
				Si contador < limite Entonces
					Escribir "Ingrese el codigo del producto:"
					Leer codigo[contador]
					Escribir "Ingrese el nombre del producto:"
					Leer nombres[contador]
					Escribir "Ingrese el precio unitario:"
					Leer precios[contador]
					Escribir "Ingrese cantidad en bodega:"
					Leer stocks[contador]
					contador <- contador + 1
					Escribir "Producto registrado."
				SiNo
					Escribir "No hay espacio para más productos."
				Fin Si
				Esperar 1 Segundo
			2:
				Si contador = 1 Entonces 
					Escribir "No hay productos por mostrar."
				SiNo
					Para i<-1 Hasta contador-1 Hacer
						Escribir i, " - Codigo: ", codigo[i], " | Producto: ", nombres[i], " | Precio: $", precios[i], " | Stock: ", stocks[i]			
					FinPara
				FinSi
				Escribir "Presione una tecla para continuar..."
				Esperar Tecla
			3:	
				Escribir "Ingrese el codigo del producto a modificar:"
				Leer modificar
				Para m<-1 Hasta contador-1 Hacer
					si modificar = codigo[m] Entonces
						Escribir "Nueva cantidad de stock:"
						Leer stocks[m]
						Escribir "Nuevo precio:"
						Leer precios[m]
						Escribir "--- Datos Modificados con exito ---"
						Escribir "Codigo: ", codigo[m], " | Producto: ", nombres[m], " | Stock: ", stocks[m]
					SiNo
						Escribir "Buscando..."
					FinSi
				FinPara
				Esperar 1 Segundo
		FinSegun
	Hasta Que eleccion = 4
FinSubProceso

SubProceso Modulo_Cesar_Movimientos
	Definir opcion_c Como Entero
	
	// Datos de inicializacion para la demo
	Dimension prod_c[100], stock_c[100], existe_c[100]
	Para i <- 1 Hasta 100 Hacer
		existe_c[i] <- Falso
	FinPara
	
	prod_c[1] <- "LAPTOP"; stock_c[1] <- 10; existe_c[1] <- Verdadero
	prod_c[2] <- "MOUSE"; stock_c[2] <- 50; existe_c[2] <- Verdadero
	
	Repetir
		Limpiar Pantalla
		Escribir "======= MOVIMIENTOS DE INVENTARIO ======="
		Escribir "1. Registrar ENTRADA"
		Escribir "2. Registrar SALIDA"
		Escribir "3. Listar productos de prueba"
		Escribir "4. Regresar al Menu Principal"
		Escribir "=========================================="
		Leer opcion_c
		
		Segun opcion_c Hacer
			1:
				Definir id_p, cant Como Entero
				Escribir "ID del producto (1-100):"
				Leer id_p
				Si id_p >= 1 y id_p <= 100 y existe_c[id_p] Entonces
					Escribir "Cantidad a ingresar:"
					Leer cant
					stock_c[id_p] <- stock_c[id_p] + cant
					Escribir "Entrada registrada. Stock actual: ", stock_c[id_p]
				SiNo
					Escribir "Error: ID no valido o producto no existe."
				FinSi
				Esperar 2 Segundos
			2:
				Escribir "ID del producto (1-100):"
				Leer id_p
				Si id_p >= 1 y id_p <= 100 y existe_c[id_p] Entonces
					Escribir "Cantidad a retirar:"
					Leer cant
					Si stock_c[id_p] >= cant Entonces
						stock_c[id_p] <- stock_c[id_p] - cant
						Escribir "Salida registrada. Stock restante: ", stock_c[id_p]
					SiNo
						Escribir "Error: Stock insuficiente."
					FinSi
				SiNo
					Escribir "Error: ID no valido."
				FinSi
				Esperar 2 Segundos
			3:
				Para i <- 1 Hasta 100 Hacer
					Si existe_c[i] Entonces
						Escribir "ID: ", i, " | ", prod_c[i], " | Stock: ", stock_c[i]
					FinSi
				FinPara
				Escribir "Presione una tecla..."
				Esperar Tecla
		FinSegun
	Hasta Que opcion_c = 4
FinSubProceso