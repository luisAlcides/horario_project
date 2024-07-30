from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Horario(models.Model):
    FORMATO_HORA_CHOICES = [
        ("AM_PM", "AM/PM"),
        ("24_HORAS", "24 Horas"),
    ]

    DIAS_SEMANA_CHOICES = [
        ("LUN", "Lunes"),
        ("MAR", "Martes"),
        ("MIE", "Miércoles"),
        ("JUE", "Jueves"),
        ("VIE", "Viernes"),
        ("SAB", "Sábado"),
        ("DOM", "Domingo"),
        ("TODOS", "Todos los días"),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    formato_hora = models.CharField(
        max_length=8, choices=FORMATO_HORA_CHOICES, default="24_HORAS"
    )  # Cambiado a 8
    dia_semana = models.CharField(
        max_length=6, choices=DIAS_SEMANA_CHOICES, default="LUN"
    )

    def __str__(self):
        return self.nombre
