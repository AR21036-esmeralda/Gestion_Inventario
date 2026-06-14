# Gestión de Inventario - Grupo 1

## Descripción

Este proyecto consiste en un sistema de gestión de inventario desarrollado en Python. El sistema permite administrar proveedores, productos y movimientos de inventario mediante menús interactivos en consola.

## Objetivo

Desarrollar un sistema de gestión de inventario que permita administrar proveedores, productos y movimientos de mercancía de forma organizada, aplicando estructuras de datos, modularización del código, validación de datos y pruebas unitarias para garantizar el correcto funcionamiento del sistema.

## Funcionalidades

### Gestión de Proveedores

Permite:

* Registrar proveedores.
* Mostrar la lista de proveedores registrados.
* Buscar proveedores por código.
* Modificar teléfono o dirección de un proveedor.
* Eliminar proveedores.

### Gestión de Productos

Permite:

* Registrar productos.
* Asociar productos a proveedores existentes.
* Mostrar productos registrados.
* Buscar productos por código.
* Modificar nombre, precio o proveedor de un producto.
* Eliminar productos.

### Movimientos de Inventario

Permite:

* Registrar entradas de mercancía.
* Registrar salidas de mercancía.
* Consultar el stock de un producto.
* Ver el listado completo de productos.
* Consultar el historial de movimientos.
* Mostrar un resumen general del inventario.
* Calcular el valor total del inventario.

## Estructura del Proyecto

```text
python/
│
├── main.py
├── MODULO_GESTION_PRODUCTOS.py
├── MODULO_GESTION_PROVEEDORES.py
├── MODULO_MOVIMIENTOS_INVENTARIO.py
└── test_modulo_movimientos_inventario.py
```

## Obtención del Proyecto

Existen dos formas de obtener una copia del repositorio desde GitHub.

### Opción 1: Descargar como archivo ZIP

1. Ingresar al repositorio en GitHub.
2. Hacer clic en el botón **Code**.
3. Seleccionar **Download ZIP**.
4. Extraer el archivo descargado en una carpeta de su computadora.

### Opción 2: Clonar el repositorio

Si tiene Git instalado, puede clonar el repositorio utilizando el siguiente comando:

```bash
git clone URL_DEL_REPOSITORIO
```

## Requisitos

Para ejecutar este proyecto es necesario tener instalado:

* Python 3.10 o superior.
* Pytest (para ejecutar las pruebas unitarias).

### Instalación de Python

1. Descargar Python desde el sitio oficial:

https://www.python.org/downloads/

2. Ejecutar el instalador.
3. Durante la instalación, marcar la opción:

```text
Add Python to PATH
```

4. Finalizar la instalación.
5. Verificar que Python se instaló correctamente ejecutando:

```bash
python --version
```

Si la instalación fue exitosa, se mostrará la versión instalada de Python.

### Instalación de Pytest

Una vez instalado Python, abrir una terminal y ejecutar:

```bash
pip install pytest
```

Para verificar la instalación:

```bash
pytest --version
```

## Ejecución del Programa

### Desde Visual Studio Code

1. Abrir Visual Studio Code.
2. Seleccionar **File → Open Folder...**.
3. Buscar la carpeta descargada del proyecto llamada **Gestion_Inventario** y abrirla.
4. En el panel lateral izquierdo, abrir la carpeta **python**.
5. Localizar y abrir el archivo **main.py**.
6. Presionar el botón **Run Python File** ubicado en la parte superior derecha.

También puede hacer clic derecho sobre el archivo **main.py** y seleccionar:

```text
Run Python File in Terminal
```

7. El sistema iniciará mostrando el menú principal.

## Ejemplo de Uso

### Registrar un proveedor

1. Seleccionar **Gestión de proveedores**.
2. Elegir **Registrar proveedor**.
3. Ingresar:

   * Código.
   * Nombre.
   * Teléfono.
   * Dirección.

### Registrar un producto

1. Seleccionar **Gestión de productos**.
2. Elegir **Registrar producto**.
3. Ingresar:

   * Código del producto.
   * Nombre.
   * Precio.
   * Stock inicial.
   * Código del proveedor.

### Registrar una entrada de mercancía

1. Seleccionar **Movimientos de inventario**.
2. Elegir **Registrar entrada**.
3. Ingresar:

   * Código del producto.
   * Cantidad.
   * Motivo (compra, devolución de cliente o ajuste).

### Registrar una salida de mercancía

1. Seleccionar **Movimientos de inventario**.
2. Elegir **Registrar salida**.
3. Ingresar:

   * Código del producto.
   * Cantidad.
   * Motivo (venta, devolución al proveedor, merma o ajuste).

## Pruebas Unitarias

El proyecto incluye dos pruebas unitarias en el archivo:

```text
test_modulo_movimientos_inventario.py
```

Para ejecutar las pruebas:

1. Abrir una terminal.
2. Ubicarse en la carpeta del proyecto.
3. Ejecutar:

```bash
pytest
```

Si las pruebas se ejecutan correctamente, se mostrará un resultado similar a:

```text
2 passed
```

## Integrantes

* Esmeralda Isabel Álvarez Rivas
* César Ezequiel Aguilar Peralta

## Tecnologías Utilizadas

* Python (implementación del sistema).
* GitHub (control de versiones y trabajo colaborativo).
* PSeInt (diseño inicial en pseudocódigo).
* Pytest (pruebas unitarias).
* Visual Studio Code (desarrollo y ejecución del proyecto).

```
```



