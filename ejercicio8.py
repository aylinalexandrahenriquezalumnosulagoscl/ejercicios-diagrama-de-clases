#Ejercicio 8: Sistema de Redes Sociales
#Clases: Usuario, Publicacion, Comentario. Relaciones: Un Usuario puede hacer múltiples
#Publicaciones, una Publicacion puede tener múltiples Comentarios.

#+-------------+        +-------------+        +-------------+
#|   Usuario   |        | Publicacion |        |  Comentario  |
#+-------------+        +-------------+        +-------------+
#| id          |1----*  | id          |        | id          |
#| nombre      |        | contenido    |        | contenido    |
#| email       |        | fecha        |        | fecha        |
#| telefono    |        | usuarioId    |        | publicacionId |
#+-------------+        +-------------+        +-------------+
#| +crearPublicacion()  | +agregarComentario()|  | +editar()    |
#| +verPublicaciones(): |+verComentarios()    |  |+eliminar():  |
#                                    
#              
