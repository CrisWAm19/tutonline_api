# Generated by Django 4.2.1 on 2023-05-20 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_alter_notificacion_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='fotoPerfil',
            field=models.ImageField(default='../img/usuarios.png', null=True, upload_to='', verbose_name='Foto de perfil'),
        ),
    ]
