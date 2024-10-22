Ejercicio 9: Sistema de Alquiler de Vehículos
Clases: Vehiculo, Cliente, Reserva. Relaciones: Un Cliente puede tener múltiples
Reservas, una Reserva está asociada a un Vehiculo.




+-------------+        +-------------+        +-------------+
|   Cliente   |        |   Reserva    |        |   Vehiculo   |
+-------------+        +-------------+        +-------------+
| id          |1----*  | id          |        | id          |
| nombre      |        | fechaInicio  |        | marca       |
| email       |        | fechaFin     |        | modelo      |
| telefono    |        | vehiculoId   |        | anio        |
+-------------+        | clienteId    |        | precioDiario|
|+crearReserva()|      |caancelar()   |        |reservar()   |
|+verReservas():|      |confirmar()   |
