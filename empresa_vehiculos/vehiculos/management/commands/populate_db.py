from django.core.management.base import BaseCommand
from vehiculos.models import Chofer, Vehiculo, RegistroContable
import random

class Command(BaseCommand):
    help = 'Carga datos inventados a la base de datos'

    def handle(self, *args, **kwargs):
        # Crear choferes
        choferes = []
        for i in range(5):
            chofer = Chofer.objects.create(
                nombre=f'Nombre{i+1}',
                apellido=f'Apellido{i+1}',
                licencia_conducir=f'LIC{i+1:04d}',
                habilitado=random.choice([True, False])
            )
            choferes.append(chofer)
            self.stdout.write(self.style.SUCCESS(f'Chofer {chofer.nombre} {chofer.apellido} creado.'))

        # Crear vehículos
        vehiculos = []
        for i in range(5):
            vehiculo = Vehiculo.objects.create(
                matricula=f'ABC{i+1:03d}',
                modelo=f'Modelo{i+1}',
                marca=f'Marca{i+1}',
                chofer=random.choice(choferes),
                habilitado=random.choice([True, False])
            )
            vehiculos.append(vehiculo)
            self.stdout.write(self.style.SUCCESS(f'Vehículo {vehiculo.marca} {vehiculo.modelo} creado.'))

        # Crear registros contables
        for vehiculo in vehiculos:
            registro = RegistroContable.objects.create(
                vehiculo=vehiculo,
                costo=random.uniform(1000, 5000)
            )
            self.stdout.write(self.style.SUCCESS(f'Registro contable para vehículo {vehiculo.matricula} creado.'))
