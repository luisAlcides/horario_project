# Generated by Django 5.0.7 on 2024-07-30 05:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('formato_hora', models.CharField(choices=[('AM_PM', 'AM/PM'), ('24_HORAS', '24 Horas')], default='24_HORAS', max_length=8)),
                ('dia_semana', models.CharField(choices=[('LUN', 'Lunes'), ('MAR', 'Martes'), ('MIE', 'Miércoles'), ('JUE', 'Jueves'), ('VIE', 'Viernes'), ('SAB', 'Sábado'), ('DOM', 'Domingo'), ('TODOS', 'Todos los días')], default='LUN', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
