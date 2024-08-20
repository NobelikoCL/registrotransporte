from django.db import models

class Chofer(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    licencia_conducir = models.CharField(max_length=20, unique=True)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Vehiculo(models.Model):
    matricula = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    chofer = models.ForeignKey(Chofer, on_delete=models.SET_NULL, null=True, blank=True)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.matricula}"

class RegistroContable(models.Model):
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)
    fecha_registro = models.DateField(auto_now_add=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Registro {self.vehiculo.matricula} - {self.fecha_registro}"
