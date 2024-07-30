from django import forms
from .models import Perfil
from .models import Horario


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["bio"]


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = [
            "nombre",
            "descripcion",
            "hora_inicio",
            "hora_fin",
            "formato_hora",
            "dia_semana",
        ]
        widgets = {
            "hora_inicio": forms.TimeInput(format="%H:%M"),
            "hora_fin": forms.TimeInput(format="%H:%M"),
        }

class HorarioBulkDeleteForm(forms.Form):
    dia_semana = forms.ChoiceField(choices=Horario.DIAS_SEMANA_CHOICES, required=False, label="Día de la Semana")
    confirm_delete_all = forms.BooleanField(required=False, label="Eliminar todos los horarios")

class HorarioBulkUpdateForm(forms.Form):
    dia_semana = forms.ChoiceField(choices=Horario.DIAS_SEMANA_CHOICES, required=True, label="Día de la Semana")
    hora_inicio = forms.TimeField(required=False, label="Nueva Hora de Inicio")
    hora_fin = forms.TimeField(required=False, label="Nueva Hora de Fin")

