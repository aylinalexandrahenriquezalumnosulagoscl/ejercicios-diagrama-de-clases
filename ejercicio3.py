Ejercicio 3: Sistema de Gestión Escolar
Clases: Estudiante, Curso, Profesor. Relaciones: Un Estudiante puede inscribirse en
múltiples Cursos, un Curso puede ser impartido por un Profesor.





+---------------------+
|     Estudiante      |
+---------------------+
| id: int             |
| nombre: string      |
| email: string       |
| telefono: string    |
+---------------------+
| + inscribirseEnCurso()         |
| + verCursosInscritos()         |
+---------------------+

            * 
            |
            |
            | 1
+---------------------+
|       Curso         |
+---------------------+
| id: int             |
| nombre: string      |
| descripcion: string |
| profesorId: int     |
+---------------------+
| + agregarEstudiante()            |
| + listarEstudiantes()            |
| + obtenerDetalles()             |
+---------------------+

            1  
            |
            |
            | *
+---------------------+
|      Profesor       |
+---------------------+
| id: int             |
| nombre: string      |
| email: string       |
| departamento: string |
+---------------------+
| + impartirCurso()                |
| + verCursosImpartidos()          |
+---------------------+
