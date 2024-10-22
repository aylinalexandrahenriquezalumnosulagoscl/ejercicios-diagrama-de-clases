Ejercicio 12: Sistema de Clases Online
Clases: Curso, Estudiante, Instructor. Relaciones: Un Estudiante puede inscribirse en
múltiples Cursos, un Instructor puede impartir múltiples Cursos.



+---------------------+
|      Paciente       |
+---------------------+
| id: int             |
| nombre: string      |
| fechaNacimiento: date |
| telefono: string    |
| email: string       |
+---------------------+
| + agendarCita()                |
| + verCitas()                   |
+---------------------+

            1
            |
            |
            | *
+---------------------+
|       Cita          |
+---------------------+
| id: int             |
| fecha: date         |
| hora: time          |
| pacienteId: int     |
| medicoId: int       |
+---------------------+
| + confirmar()                   |
| + cancelar()                    |
+---------------------+

            *  
            |
            |
            | 1
+---------------------+
|       Medico        |
+---------------------+
| id: int             |
| nombre: string      |
| especialidad: string|
| telefono: string    |
| email: string       |
+---------------------+
| + atenderCita()                |
| + verCitasAtendidas()          |
+---------------------+
