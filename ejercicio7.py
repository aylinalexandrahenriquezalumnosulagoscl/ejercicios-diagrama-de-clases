Ejercicio 7: Sistema de Atención al Cliente
Clases: Ticket, Cliente, Agente. Relaciones: Un Cliente puede crear múltiples Tickets,
un Agente puede gestionar múltiples Tickets.

+---------------------+
|       Ticket        |
+---------------------+
| id: int             |
| descripcion: string |
| estado: string      |
| fechaCreacion: date |
| clienteId: int      |
| agenteId: int       |
+---------------------+
| + abrir()                       |
| + cerrar()                      |
| + asignarAgente()              |
+---------------------+

            * 
            |
            |
            | 1
+---------------------+
|      Cliente        |
+---------------------+
| id: int             |
| nombre: string      |
| email: string       |
| telefono: string    |
+---------------------+
| + crearTicket()                 |
| + verTickets()                  |
+---------------------+

            *  
            |
            |
            | 1
+---------------------+
|       Agente        |
+---------------------+
| id: int             |
| nombre: string      |
| email: string       |
| departamento: string |
+---------------------+
| + gestionarTicket()              |
| + verTicketsAsignados()          |
+---------------------+
