from django.urls import path
from .views import home
from .views import actualizar_vehiculo, eliminar_vehiculo

urlpatterns = [
    path('', home, name='home'),
    path('actualizar-vehiculo/<int:vehiculo_id>/', actualizar_vehiculo, name='actualizar_vehiculo'),
    path('eliminar-vehiculo/<int:vehiculo_id>/', eliminar_vehiculo, name='eliminar_vehiculo'),
]
