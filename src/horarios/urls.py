# horarios/urls.py
from django.urls import path
from . import views

app_name = 'horarios'

urlpatterns = [
    path('', views.horario_list, name='horario_list'),
    path('nuevo/', views.horario_create, name='horario_create'),
    path('editar/<int:pk>/', views.horario_update, name='horario_update'),
    path('eliminar/<int:pk>/', views.horario_delete, name='horario_delete'),
    path('eliminar_masivo/', views.horario_bulk_delete, name='horario_bulk_delete'),
    path('actualizar_masivo/', views.horario_bulk_update, name='horario_bulk_update'),
    path('perfil/', views.perfil_view, name='perfil'),
]
