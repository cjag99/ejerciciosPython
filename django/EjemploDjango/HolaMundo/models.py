from django.db import models

# Create your models here.
class Author (models.Model):
    name=models.CharField (verbose_name='Nombre', # etiqueta dentro de la tabla
    max_length= 100,
    default=''
    )
    last_name=models.CharField(verbose_name='Apellido',
    max_length=150,
    default='')
    age=models.PositiveSmallIntegerField (verbose_name='Edad',
    default=0
    )
    mail=models.EmailField (verbose_name='Correo Electrónico',
    max_length=254, default='')
