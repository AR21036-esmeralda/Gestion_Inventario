Algoritmo Sistema_Gestion_Inventario_Grupo1
	// 1. DEFINICION DE VARIABLES GLOBALES (Compartidas)
	Definir nombres Como Caracter
	Definir precios Como Real
	Definir stocks, contador, eleccion, limite, codigo Como Entero
	
	limite <- 100
	Dimension codigo[limite], nombres[limite], precios[limite], stocks[limite]
	contador <- 1 // Este contador rastrea cuantos productos existen
	
	Repetir
		Limpiar Pantalla
		Escribir "================================================="
		Escribir "   SISTEMA INTEGRADO DE INVENTARIO - GRUPO 1"
		Escribir "================================================="
		Escribir "1. Modulo de Gestion de Productos (Esmeralda)"
		Escribir "2. Modulo de Movimientos de Inventario (Armando)"
		Escribir "3. Salir del Sistema"
		Escribir "-------------------------------------------------"
		Escribir "Seleccione una opcion: "
		Leer eleccion
		
		Segun eleccion Hacer
			1:
				Modulo_Esmeralda_Gestion(nombres, precios, stocks, codigo, contador)
			2:
				// Usamos el codigo que te mando Esmeralda
				Modulo_Movimientos(nombres, precios, stocks, codigo, contador)
			3:
				Escribir "Cerrando sistema... ¡Exitos en la defensa de hoy!"
			De Otro Modo:
				Escribir "Opcion no valida."
				Esperar 2 Segundos
		Fin Segun
	Hasta Que eleccion = 3
FinAlgoritmo

// --- MODULO DE ESMERALDA ---
SubProceso Modulo_Esmeralda_Gestion(nombres Por Referencia, precios Por Referencia, stocks Por Referencia, codigo Por Referencia, contador Por Referencia)
	Definir eleccion_e, i Como Entero
	Repetir
		Limpiar Pantalla
		Escribir "--------MODULO GESTION DE PRODUCTOS-------" 
		Escribir "1. Crear producto"
		Escribir "2. Mostrar Productos"
		Escribir "3. Regresar al Menu Principal"
		Leer eleccion_e
		Segun eleccion_e Hacer
			1: 
				Escribir "Ingrese el codigo del producto:"
				Leer codigo[contador]
				Escribir "Ingrese el nombre del producto:"
				Leer nombres[contador]
				Escribir "Ingrese el precio unitario:"
				Leer precios[contador]
				Escribir "Ingrese cantidad inicial de stock:"
				Leer stocks[contador]
				contador <- contador + 1
				Escribir "Producto registrado con exito."
				Esperar 1 Segundo
			2:
				Si contador = 1 Entonces
					Escribir "No hay productos registrados."
				SiNo
					Para i<-1 Hasta contador-1 Hacer
						Escribir i, "- Codigo: ", codigo[i], " | Producto: ", nombres[i], " | Stock: ", stocks[i]
					FinPara
				FinSi
				Escribir "Presione una tecla para continuar..."
				Esperar Tecla
		FinSegun
	Hasta Que eleccion_e = 3
FinSubProceso

// --- TU MODULO (EL QUE TE MANDO ELLA) ---
SubProceso Modulo_Movimientos(nombres Por Referencia, precios Por Referencia, stocks Por Referencia, codigo Por Referencia, contador Por Referencia)
	
	Definir opcion, i, id, cantidad, encontrado Como Entero
	
	Repetir
		Limpiar Pantalla
		Escribir "---- MOVIMIENTOS ----"
		Escribir "1. Entrada"
		Escribir "2. Salida"
		Escribir "3. Ver productos"
		Escribir "4. Regresar"
		Leer opcion
		
		Segun opcion Hacer
			
			1:
				Escribir "Codigo producto:"
				Leer id
				
				encontrado <- 0
				
				Para i <- 1 Hasta contador-1 Hacer
					Si codigo[i] = id Entonces
						encontrado <- 1
						
						Escribir "Cantidad a ingresar:"
						Leer cantidad
						
						stocks[i] <- stocks[i] + cantidad
						
						Escribir "Nuevo stock:", stocks[i]
					FinSi
				FinPara
				
				Si encontrado = 0 Entonces
					Escribir "Producto no encontrado"
				FinSi
				
				Esperar 3 Segundos
				
			2:
				Escribir "Codigo producto:"
				Leer id
				
				encontrado <- 0
				
				Para i <- 1 Hasta contador-1 Hacer
					Si codigo[i] = id Entonces
						encontrado <- 1
						
						Escribir "Cantidad a retirar:"
						Leer cantidad
						
						Si stocks[i] >= cantidad Entonces
							stocks[i] <- stocks[i] - cantidad
							Escribir "Stock restante:", stocks[i]
						SiNo
							Escribir "Stock insuficiente"
						FinSi
					FinSi
				FinPara
				
				Si encontrado = 0 Entonces
					Escribir "Producto no encontrado"
				FinSi
				
				Esperar 1 Segundo
				
			3:
				Para i <- 1 Hasta contador-1 Hacer
					Escribir "Codigo:", codigo[i], " | ", nombres[i], " | Stock:", stocks[i]
				FinPara
				Esperar Tecla
				
		FinSegun
		
	Hasta Que opcion = 4
	
FinSubProceso
