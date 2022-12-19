from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Inscritos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    fechaInscripcion = models.DateField()
    institucion = models.CharField(max_length=50)
    horaInscripcion = models.CharField(max_length=10)
    estado = models.CharField(max_length=20)
    observacion = models.CharField(max_length=150, null=True)

class Institucion(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    codigo = models.IntegerField()
    direccion = models.CharField(max_length=50)




# Para cada Inscrito mínimo se debe considerar, su ID, nombre de la persona, teléfono,
# fecha inscripción, institución, la hora de inscripción, el estado (RESERVADO, COMPLETADA,
# ANULADA, NO ASISTEN) y una observación