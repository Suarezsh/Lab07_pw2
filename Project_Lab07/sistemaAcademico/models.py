from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.
class Alumno(models.Model):
    idAlumno = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cui = models.IntegerField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Curso(models.Model):
    idCurso = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    creditos = models.IntegerField()

    def __str__(self):
        return self.nombre

class NotasAlumnoPorCurso(models.Model):
    idNotasAlumnoPorCurso = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Nota de \"{self.alumno}\" en \"{self.curso}\": {self.nota}"