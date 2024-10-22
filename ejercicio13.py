Ejercicio 13: Sistema de Gestión de Eventos
Clases: Evento, Participante, Ubicacion. Relaciones: Un Evento puede tener múltiples
Participantes, un Evento se lleva a cabo en una Ubicacion.


+---------------------+
|       Evento        |
+---------------------+
| id: int             |
| nombre: string      |
| descripcion: string |
| fecha: date         |
| ubicacionId: int    |
+---------------------+
| + agregarParticipante()           |
| + listarParticipantes()           |
| + obtenerDetalles()               |
+---------------------+

            * 
            |
            |
            | 1
+---------------------+
|    Participante      |
+---------------------+
| id: int             |
| nombre: string      |
| email: string       |
| telefono: string    |
+---------------------+
| + registrarse()                |
| + verEventosParticipados()     |
+---------------------+

            1  
            |
            |
            | 1
+---------------------+
|     Ubicacion        |
+---------------------+
| id: int             |
| direccion: string   |
| capacidad: int      |
| tipo: string        |
+---------------------+
| + obtenerDetalles()              |
| + verificarDisponibilidad()       |
+---------------------+
