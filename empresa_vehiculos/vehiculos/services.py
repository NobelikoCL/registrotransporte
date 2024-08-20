from .models import Vehiculo, Chofer, RegistroContable
from django.core.exceptions import ObjectDoesNotExist

# Servicio para crear un vehículo
def crear_vehiculo(matricula, modelo, marca, chofer_id=None):
    chofer = None
    if chofer_id:
        try:
            chofer = Chofer.objects.get(id=chofer_id)
        except ObjectDoesNotExist:
            raise ValueError("Chofer no encontrado")
    vehiculo = Vehiculo.objects.create(
        matricula=matricula,
        modelo=modelo,
        marca=marca,
        chofer=chofer
    )
    return vehiculo

# Servicio para crear un chofer
def crear_chofer(nombre, apellido, licencia_conducir):
    chofer = Chofer.objects.create(
        nombre=nombre,
        apellido=apellido,
        licencia_conducir=licencia_conducir
    )
    return chofer

# Servicio para crear un registro contable
def crear_registro_contable(vehiculo_id, costo):
    try:
        vehiculo = Vehiculo.objects.get(id=vehiculo_id)
    except ObjectDoesNotExist:
        raise ValueError("Vehículo no encontrado")
    
    registro = RegistroContable.objects.create(
        vehiculo=vehiculo,
        costo=costo
    )
    return registro

# Servicio para deshabilitar un chofer
def deshabilitar_chofer(chofer_id):
    try:
        chofer = Chofer.objects.get(id=chofer_id)
        chofer.habilitado = False
        chofer.save()
    except ObjectDoesNotExist:
        raise ValueError("Chofer no encontrado")

# Servicio para habilitar un chofer
def habilitar_chofer(chofer_id):
    try:
        chofer = Chofer.objects.get(id=chofer_id)
        chofer.habilitado = True
        chofer.save()
    except ObjectDoesNotExist:
        raise ValueError("Chofer no encontrado")

# Servicio para deshabilitar un vehículo
def deshabilitar_vehiculo(vehiculo_id):
    try:
        vehiculo = Vehiculo.objects.get(id=vehiculo_id)
        vehiculo.habilitado = False
        vehiculo.save()
    except ObjectDoesNotExist:
        raise ValueError("Vehículo no encontrado")

# Servicio para habilitar un vehículo
def habilitar_vehiculo(vehiculo_id):
    try:
        vehiculo = Vehiculo.objects.get(id=vehiculo_id)
        vehiculo.habilitado = True
        vehiculo.save()
    except ObjectDoesNotExist:
        raise ValueError("Vehículo no encontrado")

# Servicio para obtener un vehículo por su ID
def obtener_vehiculo(vehiculo_id):
    try:
        vehiculo = Vehiculo.objects.get(id=vehiculo_id)
        return vehiculo
    except ObjectDoesNotExist:
        raise ValueError("Vehículo no encontrado")

# Servicio para obtener un chofer por su ID
def obtener_chofer(chofer_id):
    try:
        chofer = Chofer.objects.get(id=chofer_id)
        return chofer
    except ObjectDoesNotExist:
        raise ValueError("Chofer no encontrado")

# Servicio para asignar un chofer a un vehículo
def asignar_chofer_a_vehiculo(vehiculo_id, chofer_id):
    try:
        vehiculo = Vehiculo.objects.get(id=vehiculo_id)
        chofer = Chofer.objects.get(id=chofer_id)
        vehiculo.chofer = chofer
        vehiculo.save()
    except ObjectDoesNotExist:
        raise ValueError("Vehículo o chofer no encontrado")

# Servicio para imprimir datos de todos los vehículos
def imprimir_datos_vehiculos():
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        print(f"Matricula: {vehiculo.matricula}, Modelo: {vehiculo.modelo}, Marca: {vehiculo.marca}, Chofer: {vehiculo.chofer}, Habilitado: {vehiculo.habilitado}")
