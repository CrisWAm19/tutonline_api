# Generated by Django 4.2.1 on 2023-05-10 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_delete_prueba'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='fotoPerfil',
            field=models.BinaryField(null=True, verbose_name='Foto de perfil'),
        ),
        migrations.AlterField(
            model_name='profesion',
            name='tituloValidado',
            field=models.CharField(default='Pendiente', max_length=9, null=True, verbose_name='Titulo validado'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='fotoPerfil',
            field=models.BinaryField(null=True, verbose_name='Foto de perfil'),
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('idClase', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Clase')),
                ('fecha', models.DateField(verbose_name='Fecha de la clase')),
                ('hora', models.TimeField(verbose_name='Hora de la clase')),
                ('modalidad', models.TextField(max_length=10, verbose_name='Modalidad')),
                ('idAsignaturaClase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.asignatura')),
                ('rutProfClase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profesor')),
            ],
            options={
                'verbose_name': 'Clase',
                'verbose_name_plural': 'Clases',
                'db_table': 'Clase',
            },
        ),
    ]
