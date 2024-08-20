from django.shortcuts import render
from .models import Vehiculo, Chofer, RegistroContable
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Vehiculo, Chofer, RegistroContable

def home(request):
    vehiculos = Vehiculo.objects.all()
    choferes = Chofer.objects.all()
    registros = RegistroContable.objects.all()

    context = {
        'vehiculos': vehiculos,
        'choferes': choferes,
        'registros': registros,
    }
    return render(request, 'vehiculos/home.html', context)

def actualizar_vehiculo(request, vehiculo_id):
    if request.method == 'POST':
        try:
            vehiculo = Vehiculo.objects.get(id=vehiculo_id)
            campo = request.POST.get('campo')
            valor = request.POST.get('valor')

            if campo == 'matricula':
                vehiculo.matricula = valor
            elif campo == 'modelo':
                vehiculo.modelo = valor
            elif campo == 'marca':
                vehiculo.marca = valor
            # Añadir más campos si es necesario

            vehiculo.save()
            return JsonResponse({'status': 'success', 'message': 'Vehículo actualizado correctamente'})
        except Vehiculo.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Vehículo no encontrado'})
    return HttpResponseNotAllowed(['POST'])

def eliminar_vehiculo(request, vehiculo_id):
    if request.method == 'POST':
        try:
            vehiculo = Vehiculo.objects.get(id=vehiculo_id)
            vehiculo.delete()
            return JsonResponse({'status': 'success', 'message': 'Vehículo eliminado correctamente'})
        except Vehiculo.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Vehículo no encontrado'})
    return HttpResponseNotAllowed(['POST'])
