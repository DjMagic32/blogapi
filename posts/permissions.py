from rest_framework import permissions

class IsAuthorOrReadOnly (permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Se permiten permisos de solo lectura para cualquier solicitud
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Los permisos de escritura solo están permitidos para el autor de una publicación
        return obj.author == request.user

#Importamos permisos en la parte superior y luego
#creamos una clase personalizada IsAuthorOrReadOnly que extiende BasePermission.

#Luego anulamos has_object_permission.

#Si una solicitud contiene verbos HTTP incluidos en SAFE_METHODS,
#una tupla que contiene GET, OPTIONS y HEAD, entonces es una solicitud de solo lectura y se otorga permiso.
#De lo contrario, la solicitud es para una escritura de algún tipo,
#lo que significa actualizar el recurso de la API para crear,
#eliminar o editar la funcionalidad.

#En ese caso, verificamos si el autor del objeto en cuestión,
#que es nuestra publicación de blog obj.author, 
#coincide con el usuario que realiza la solicitud request.user.

#De vuelta en el archivo views.py 
#deberíamos importar IsAuthorOrReadOnly 
#y luego podemos agregar allow_classes para PostDetail.