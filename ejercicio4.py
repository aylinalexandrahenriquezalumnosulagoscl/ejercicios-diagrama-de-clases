Ejercicio 4: Sistema de Reservas de Hotel
Clases: Habitacion, Reserva, Cliente. Relaciones: Un Cliente puede hacer múltiples
Reservas, una Reserva está asociada a una Habitacion.

+---------------------+
|      Cliente        |
+---------------------+
| id: int             |
| nombre: string      |
| email: string       |
| telefono: string    |
+---------------------+
| + hacerReserva()                |
| + verReservas()                 |
+---------------------+

            1
            |
            |
            | *
+---------------------+
|      Reserva        |
+---------------------+
| id: int             |
| fechaInicio: date   |
| fechaFin: date      |
| clienteId: int      |
| habitacionId: int   |
+---------------------+
| + confirmar()                   |
| + cancelar()                    |
| + obtenerDetalles()             |
+---------------------+

            1  
            |
            |
            | *
+---------------------+
|     Habitacion      |
+---------------------+
| id: int             |
| tipo: string        |
| precio: float       |
| estado: string      |
+---------------------+
| + reservar()                     |
| + liberar()                      |
| + obtenerDetalles()              |
+---------------------+

Cliente tiene una relación 1 ---- * con Reserva, indicando que un cliente puede hacer múltiples reservas.
Reserva tiene una relación 1 ---- * con Habitacion, indicando que una reserva está asociada a una habitación.
