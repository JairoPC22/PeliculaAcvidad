from django.db import models


class Compania(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=20)
    direccion = models.CharField(verbose_name="Direccion", max_length=120)

    def __str__(self):
        return self.nombre


class Actor(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=22)
    fechaNacimiento = models.DateField(verbose_name="Fecha de Nacimiento")

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(verbose_name="Titulo", max_length=50)
    lanzamiento = models.IntegerField(verbose_name="Año de lazamiento")
    tamanio = models.DecimalField(verbose_name="Duracion en minutos", decimal_places=2, max_digits=5)
    sinopsis = models.TextField(verbose_name="Sinopsis", max_length=300)
    IDCompania = models.ForeignKey('Compania', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Frase(models.Model):
    IDactor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    IDpelicula = models.ForeignKey('Pelicula', on_delete=models.CASCADE)
    frase = models.CharField(verbose_name="Frase", max_length=300)

    def __str__(self):
        return self.IDactor, " " + self.frase


class PeliculaActor(models.Model):
    IDpelicula = models.ForeignKey('Pelicula', on_delete=models.CASCADE)
    IDActor = models.ForeignKey('Actor', on_delete=models.CASCADE)

    def __str__(self):
        return self.IDpelicula, " ", self.IDActor


GenerPeli = {('Acción', 'Acción'), ('Aventuras', 'Aventuras'), ('Ciencia Ficción', 'Ciencia Ficción'),
             ('Comedia', 'Comedia'), ('Drama', 'Drama'), ('Fantasía', 'Fantasía'), ('Musical', 'Musical'),
             ('Suspenso', 'Suspenso'), ('Terror', 'Terror'), ('Comedia Romantica', 'Comedia Romantica'),
             ('Comedia Dramatica', 'Comedia Dramatica')}


class Genero(models.Model):
    IDpeliculas = models.ForeignKey('Pelicula', on_delete=models.CASCADE)
    genero = models.CharField(choices=GenerPeli, verbose_name='Genero de la pelicula', max_length=20)

    def __str__(self):
        return self.IDpeliculas, ' ' + self.genero


class Director(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    fechaNacimiento = models.DateField(verbose_name="Fecha de Nacimiento")

    def __str__(self):
        return self.nombre


class PeliDirector(models.Model):
    IDpelicula = models.ForeignKey('Pelicula', on_delete=models.CASCADE)
    IDdirector = models.ForeignKey('Director', on_delete=models.CASCADE)

    def __str__(self):
        return self.IDpelicula, " ", self.IDdirector


class Usuario(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    apellido = models.CharField(verbose_name="Apellidos", max_length=156)
    usuario = models.CharField(verbose_name="Usuario", max_length=200, unique=True)
    contrasena = models.CharField(verbose_name="Contraseña", max_length=15)

    def __str__(self):
        return self.usuario
