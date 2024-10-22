Ejercicio 6: Sistema de Gestión de Proyectos
Clases: Proyecto, Empleado, Tarea. Relaciones: Un Proyecto puede tener múltiples
Tareas, un Empleado puede estar asignado a múltiples Proyectos.

+---------------------+
|      Proyecto       |
+---------------------+
| id: int             |
| nombre: string      |
| descripcion: string |
| fechaInicio: date   |
| fechaFin: date      |
+---------------------+
| + agregarTarea()                |
| + listarTareas()                |
| + obtenerDetalles()             |
+---------------------+

            * 
            |
            |
            | 1
+---------------------+
|       Tarea         |
+---------------------+
| id: int             |
| nombre: string      |
| descripcion: string |
| estado: string      |
| proyectoId: int     |
+---------------------+
| + marcarComoCompleta()          |
| + obtenerDetalles()             |
+---------------------+

            *  
            |
            |
            | 1
+---------------------+
|      Empleado       |
+---------------------+
| id: int             |
| nombre: string      |
| email: string       |
| telefono: string    |
| puesto: string      |
+---------------------+
| + asignarProyecto()               |
| + verProyectosAsignados()         |
+---------------------+
Cliente tiene una relación 1 ---- * con Ticket, indicando que un cliente puede crear múltiples tickets.
Agente tiene una relación 1 ---- * con Ticket, indicando que un agente puede gestionar múltiples tickets.
