from rest_framework import generics, permissions #se agregaron las permisiones de la API
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

#El último paso es crear nuestras vistas. Django REST Framework tiene varias vistas genéricas que son útiles. Ya hemos utilizado ListAPIView tanto en la biblioteca como en las API de Todos para crear una colección de puntos finales de solo lectura, esencialmente una lista de todas las instancias del modelo.
#En la API de Todos también usamos RetrieveAPIView para un único punto final de solo lectura, que es análogo a una vista detallada en Django tradicional.
#Para nuestra API de blog, queremos enumerar todas las publicaciones de blog disponibles como un punto final de lectura y escritura, lo que significa usar ListCreateAPIView, que es similar a ListAPIView que hemos usado anteriormente, pero permite escrituras.
#También queremos que las publicaciones individuales del blog estén disponibles para ser leídas, actualizadas o eliminadas. Y efectivamente, hay una vista genérica de Django REST Framework incorporada solo para este propósito: RetrieveUpdateDestroyAPIView.
#Eso es lo que usaremos aquí.
#Actualice el archivo views.py de la siguiente manera.

class PostList (generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly) #agregamos los permisos customizados
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#En la parte superior del archivo, importamos genéricos de Django REST Framework, así como nuestros modelos y archivos de serializadores. Luego creamos dos vistas.
#PostList usa genericListCreateAPIView mientras que PostDetail usa RetrieveUpdateDestroyAPIView.
#Es bastante sorprendente que todo lo que tenemos que hacer es actualizar nuestra vista genérica para cambiar radicalmente el comportamiento de un punto final de API determinado.
#Esta es la ventaja de usar un marco con todas las funciones como Django REST Framework: 
#toda esta funcionalidad está disponible, probada y simplemente funciona. Como desarrolladores,
#no tenemos que reinventar la rueda aquí.
#Nuestra API ahora está completa y realmente no tuvimos que escribir mucho código por nuestra cuenta.
#Realizaremos mejoras adicionales a nuestra API en los próximos capítulos, 
#pero vale la pena apreciar que ya realiza la lista básica y la funcionalidad CRUD que deseamos.
#Es hora de probar las cosas con la API navegable de Django Rest Framework.

#Estas 'permisiones' puestas en estas vistas son a nivel de vista mas no a nivel de proyecto 
#Por lo tanto, en este punto, solo los usuarios registrados pueden ver nuestra API. 
#Si vuelve a iniciar sesión con su cuenta de superusuario o de usuario de prueba, 
#se podrá acceder a los puntos finales de la API.

#Pero piense en lo que sucede a medida que la API crece en complejidad. 
#Es probable que tengamos muchas más vistas y puntos finales en el futuro.

#Añadiendo un permiso_clases dedicado
#a cada vista parece repetitivo si queremos establecer la misma configuración de permisos
#en toda nuestra API.

#¿No sería mejor cambiar nuestros permisos una vez, idealmente a nivel de proyecto, 
#en lugar de hacerlo para todas y cada una de las vistas?