# Generated by Django 4.2.1 on 2023-06-01 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_user_apellidomaterno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesion',
            name='tituloValidado',
            field=models.CharField(choices=[('No', 'No'), ('Si', 'Si'), ('En proceso', 'En proceso')], default='En espera', max_length=10, null=True, verbose_name='Titulo validado'),
        ),
    ]
