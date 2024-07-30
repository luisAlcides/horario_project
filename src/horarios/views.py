# horarios/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Horario
from .forms import HorarioForm, PerfilForm, HorarioBulkDeleteForm, HorarioBulkUpdateForm
from django.urls import reverse_lazy

@login_required
def perfil_view(request):
    perfil = request.user.perfil
    if request.method == "POST":
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect("perfil")
    else:
        form = PerfilForm(instance=perfil)
    return render(request, "horarios/perfil.html", {"form": form})

@login_required
def horario_list(request):
    horarios = Horario.objects.all()
    dias_semana = ["LUN", "MAR", "MIE", "JUE", "VIE", "SAB", "DOM"]
    horarios_agrupados = {}

    for horario in horarios:
        if horario.nombre not in horarios_agrupados:
            horarios_agrupados[horario.nombre] = []
        horarios_agrupados[horario.nombre].append(horario)

    return render(
        request,
        "horarios/horario_list.html",
        {"horarios": horarios_agrupados, "dias_semana": dias_semana},
    )

@login_required
def horario_create(request):
    if request.method == "POST":
        form = HorarioForm(request.POST)
        if form.is_valid():
            horario = form.save()
            if horario.dia_semana == "TODOS":
                dias_semana = ["LUN", "MAR", "MIE", "JUE", "VIE", "SAB", "DOM"]
                for dia in dias_semana:
                    horario.pk = None
                    horario.dia_semana = dia
                    horario.save()
            return redirect("horarios:horario_list")
    else:
        form = HorarioForm()
    return render(request, "horarios/horario_form.html", {"form": form})

@login_required
def horario_update(request, pk):
    horario = get_object_or_404(Horario, pk=pk)
    if request.method == "POST":
        form = HorarioForm(request.POST, instance=horario)
        if form.is_valid():
            form.save()
            return redirect("horarios:horario_list")
    else:
        form = HorarioForm(instance=horario)
    return render(request, "horarios/horario_form.html", {"form": form})

@login_required
def horario_delete(request, pk):
    horario = get_object_or_404(Horario, pk=pk)
    if request.method == "POST":
        horario.delete()
        return redirect("horarios:horario_list")
    return render(request, "horarios/horario_confirm_delete.html", {"horario": horario})

@login_required
def horario_bulk_delete(request):
    if request.method == "POST":
        form = HorarioBulkDeleteForm(request.POST)
        if form.is_valid():
            dia_semana = form.cleaned_data.get('dia_semana')
            confirm_delete_all = form.cleaned_data.get('confirm_delete_all')

            if confirm_delete_all:
                Horario.objects.all().delete()
            elif dia_semana:
                Horario.objects.filter(dia_semana=dia_semana).delete()

            return redirect("horarios:horario_list")
    else:
        form = HorarioBulkDeleteForm()
    return render(request, "horarios/horario_bulk_delete.html", {"form": form})

@login_required
def horario_bulk_update(request):
    if request.method == "POST":
        form = HorarioBulkUpdateForm(request.POST)
        if form.is_valid():
            dia_semana = form.cleaned_data.get('dia_semana')
            hora_inicio = form.cleaned_data.get('hora_inicio')
            hora_fin = form.cleaned_data.get('hora_fin')

            horarios = Horario.objects.filter(dia_semana=dia_semana)
            for horario in horarios:
                if hora_inicio:
                    horario.hora_inicio = hora_inicio
                if hora_fin:
                    horario.hora_fin = hora_fin
                horario.save()

            return redirect("horarios:horario_list")
    else:
        form = HorarioBulkUpdateForm()
    return render(request, "horarios/horario_bulk_update.html", {"form": form})
