from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Publicacion

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion')  # Muestra estas columnas en la lista de publicaciones.
    search_fields = ('titulo', 'contenido', 'autor__username')  # Permite buscar por título, contenido o autor.
    list_filter = ('autor', 'fecha_publicacion')  # Permite filtrar por autor y fecha.
    ordering = ('-fecha_publicacion',)  # Ordena las publicaciones de más recientes a más antiguas.

