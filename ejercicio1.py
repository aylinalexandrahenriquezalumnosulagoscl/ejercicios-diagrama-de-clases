Ejercicio 1: Sistema de Biblioteca
Clases: Libro, Usuario, Prestamo. Relaciones: Un Usuario puede tener múltiples
Prestamos, un Libro puede estar en múltiples Prestamos.

+---------------------+
|        Libro        |
+---------------------+
| id: int             |
| titulo: string      |
| autor: string       |
| fechaPublicacion: date |
| disponible: boolean  |
+---------------------+
| + marcarComoPrestado()         |
| + marcarComoDisponible()        |
| + obtenerDetalles()            |
+---------------------+

            * 
            |
            |
            | *
+---------------------+
|      Prestamo       |
+---------------------+
| id: int             |
| fechaPrestamo: date |
| fechaDevolucion: date |
| usuarioId: int      |
| libroId: int        |
+---------------------+
| + confirmarPrestamo()           |
| + devolverLibro()               |
| + obtenerDetalles()             |
+---------------------+

            1  
            |
            |
            | *
+---------------------+
|       Usuario       |
+---------------------+
| id: int             |
| nombre: string      |
| email: string       |
| telefono: string    |
+---------------------+
| + solicitarPrestamo()            |
| + verPrestamos()                 |
+---------------------+

Usuario tiene una relación 1 ---- * con Prestamo, indicando que un usuario puede tener múltiples préstamos.
Libro tiene una relación 1 ---- * con Prestamo, indicando que un libro puede estar en múltiples préstamos.
