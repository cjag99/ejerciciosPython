from django.db import models

# Create your models here.
class EnglishLevel(models.TextChoices):
    A1 = 'A1', 'A1'
    A2 = 'A2', 'A2'
    B1 = 'B1', 'B1'
    B2 = 'B2', 'B2'
    C1 = 'C1', 'C1'
    C2 = 'C2', 'C2'

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
    english_level=models.CharField(verbose_name='Nivel de Inglés',
    max_length=2, choices=EnglishLevel.choices,
    default=EnglishLevel.A1)

    def __str__(self):
        return f'{self.name} {self.last_name}'