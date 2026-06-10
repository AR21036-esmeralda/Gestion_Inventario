# Gestión de Inventario - Grupo 1

# Descripción del Proyecto
Este sistema CLI desarrollado en Python permite la administración integral de un catálogo de productos y sus proveedores. El objetivo es automatizar el registro de entradas y salidas de stock, garantizando la integridad de los datos y evitando existencias negativas.


## Entrega #1 - Pseudocódigo

# Funcionalidades Principales 
**Módulo de Gestión de Productos:** Registro, consulta y actualización de la información base de los productos.
**Módulo de Movimientos de Inventario:** Control de entradas y salidas de stock con validación de stock.
**Integración de Datos:** Lógica para mantener la coherencia entre el catálogo y los movimientos realizados.


## Entrega #2 – Implementación en Python

En esta fase se realizó la transición del diseño en pseudocódigo a una implementación funcional en Python, enfocándose en la estructura modular, la organización del código y la lógica CRUD. El sistema fue desarrollado como una aplicación CLI (interfaz por consola), permitiendo la interacción del usuario mediante menús y posteriormente integrando los módulos en un solo sistema.

---

## Módulo de Gestión de Proveedores

Este módulo permite administrar la información de los proveedores del sistema, quienes son necesarios para la correcta gestión de los productos.

### Funcionalidades:
- Registrar proveedores  
- Mostrar lista de proveedores registrados  
- Buscar proveedores por código  
- Actualizar información de proveedores (teléfono y dirección)  
- Eliminar proveedores  

---

## Módulo de Gestión de Productos

Este módulo permite administrar el catálogo de productos del sistema, asegurando el control de inventario y la relación con proveedores.

### Funcionalidades:
- Registrar productos asociados a un proveedor  
- Mostrar lista de productos registrados  
- Buscar productos por código  
- Actualizar información de productos (precio y stock)  
- Eliminar productos  

### Relación entre módulos:
Para registrar un producto es obligatorio que el proveedor exista previamente en el sistema, garantizando la integridad de los datos y la correcta asociación entre entidades.

---

## Integración del Sistema

Los módulos de productos y proveedores fueron desarrollados en archivos independientes y posteriormente integrados en una sola aplicación CLI. Esto permite que ambos módulos funcionen dentro de un menú principal, facilitando la gestión completa del sistema de inventario.

---

## Integrantes
* Esmeralda Isabel Alvarez Rivas
* Cesar Ezequiel Aguilar Peralta
* Luis Armando Argueta Villalobos

## Tecnologías Utilizadas
- Python (implementación del sistema)
- GitHub (control de versiones y trabajo colaborativo)
- PSeInt (diseño inicial en pseudocódigo)





