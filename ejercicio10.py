Ejercicio 10: Sistema de Gestión de Inventario
Clases: Producto, Categoria, Proveedor. Relaciones: Un Producto pertenece a una
Categoria, un Proveedor puede suministrar múltiples Productos.


+---------------------+
|      Producto       |
+---------------------+
| id: int             |
| nombre: string      |
| descripcion: string |
| precio: float       |
| cantidad: int       |
| categoriaId: int    |
| proveedorId: int    |
+---------------------+
| + actualizarCantidad()         |
| + cambiarPrecio()              |
| + asociarCategoria()           |
+---------------------+

            1
            |
            |
            | 1
+---------------------+
|      Categoria      |
+---------------------+
| id: int             |
| nombre: string      |
| descripcion: string |
+---------------------+
| + agregarProducto()              |
| + listarProductos()              |
+---------------------+

            1
            |
            |
            | *
+---------------------+
|      Proveedor      |
+---------------------+
| id: int             |
| nombre: string      |
| email: string       |
| telefono: string    |
+---------------------+
| + suministrarProducto()          |
| + listarProductosSuministrados() |
+---------------------+
