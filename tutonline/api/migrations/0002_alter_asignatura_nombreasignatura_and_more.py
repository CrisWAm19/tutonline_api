# Generated by Django 4.2.1 on 2023-06-01 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='nombreAsignatura',
            field=models.CharField(max_length=30, unique=True, verbose_name='Nombre de la asignatura'),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='nombreCarrera',
            field=models.CharField(max_length=40, unique=True, verbose_name='Nombre de la carrera'),
        ),
    ]