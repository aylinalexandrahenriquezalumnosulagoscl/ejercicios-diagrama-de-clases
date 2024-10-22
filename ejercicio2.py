Ejercicio 2: Sistema de Ventas
Clases: Producto, Cliente, Factura. Relaciones: Un Cliente puede tener múltiples
Facturas, una Factura puede incluir múltiples Productos.

+---------------------+
|      Producto       |
+---------------------+
| id: int             |
| nombre: string      |
| descripcion: string |
| precio: float       |
| stock: int          |
+---------------------+
| + actualizarStock()             |
| + obtenerDetalles()             |
+---------------------+

            * 
            |
            |
            | 1
+---------------------+
|      Factura        |
+---------------------+
| id: int             |
| fecha: date         |
| clienteId: int      |
+---------------------+
| + agregarProducto()              |
| + eliminarProducto()             |
| + calcularTotal()                |
+---------------------+

            1  
            |
            |
            | *
+---------------------+
|      Cliente        |
+---------------------+
| id: int             |
| nombre: string      |
| email: string       |
| telefono: string    |
+---------------------+
| + crearFactura()                 |
| + verFacturas()                 |
+---------------------+

Cliente tiene una relación 1 ---- * con Factura, indicando que un cliente puede tener múltiples facturas.
Factura tiene una relación 1 ---- * con Producto, indicando que una factura puede incluir múltiples productos.
