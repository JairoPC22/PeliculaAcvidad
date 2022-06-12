from django.contrib import admin
from .models import Director, PeliDirector, Pelicula, PeliculaActor, Actor, Genero, Frase, Usuario, Compania

# Register your models here.


admin.site.register(Frase)
admin.site.register(Genero)
admin.site.register(Compania)
admin.site.register(Actor)
admin.site.register(PeliDirector)
admin.site.register(Director)
admin.site.register(PeliculaActor)
admin.site.register(Usuario)
admin.site.register(Pelicula)
