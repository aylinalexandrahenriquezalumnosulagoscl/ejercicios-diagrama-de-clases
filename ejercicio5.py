Ejercicio 5: Sistema de Compras en Línea
Clases: Producto, Carrito, Usuario. Relaciones: Un Usuario puede tener un Carrito, un
Carrito puede contener múltiples Productos.

+---------------------+
|      Usuario        |
+---------------------+
| id: int             |
| nombre: string      |
| email: string       |
| telefono: string    |
+---------------------+
| + crearCarrito()               |
| + verCarrito()                 |
| + realizarCompra()              |
+---------------------+

            1
            |
            |
            | 1
+---------------------+
|      Carrito        |
+---------------------+
| id: int             |
| usuarioId: int      |
+---------------------+
| + agregarProducto()              |
| + eliminarProducto()             |
| + listarProductos()              |
+---------------------+

            *  
            |
            |
            | 1
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

Usuario tiene una relación 1 ---- 1 con Carrito, indicando que un usuario puede tener un carrito.
Carrito tiene una relación 1 ---- * con Producto, indicando que un carrito puede contener múltiples productos.
