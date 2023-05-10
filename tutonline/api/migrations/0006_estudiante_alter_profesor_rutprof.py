# Generated by Django 4.2.1 on 2023-05-10 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_profesione_profesion'),
    ]

    operations = [
        migrations.CreateModel(
            name='estudiante',
            fields=[
                ('rutEst', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Rut Estudiante')),
                ('nombreEst', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellidoPaternoEst', models.CharField(max_length=20, verbose_name='Apellido Paterno')),
                ('apellidoMaternoEst', models.CharField(max_length=20, verbose_name='Apellido Materno')),
                ('fechaNacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('correoEst', models.CharField(max_length=35, verbose_name='Correo')),
                ('contrasenaEst', models.CharField(max_length=12, verbose_name='Contrasenia')),
                ('numeroTelefonoEst', models.IntegerField()),
                ('regionEst', models.CharField(max_length=30, verbose_name='Region')),
                ('comunaEst', models.CharField(max_length=30, verbose_name='Comuna')),
                ('fotoPerfil', models.BinaryField(verbose_name='Foto de perfil')),
            ],
        ),
        migrations.AlterField(
            model_name='profesor',
            name='rutProf',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Rut Profesor'),
        ),
    ]
