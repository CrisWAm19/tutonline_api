# Generated by Django 4.2.1 on 2023-05-17 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_notificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificacion',
            name='descripcion',
            field=models.CharField(max_length=100, verbose_name='Descripcion'),
        ),
    ]
