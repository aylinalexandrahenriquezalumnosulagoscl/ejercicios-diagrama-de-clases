Ejercicio 11: Sistema de Hospital
Clases: Paciente, Medico, Cita. Relaciones: Un Paciente puede tener múltiples Citas, un
Medico puede atender múltiples Citas.


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
