# Generated by Django 4.2.1 on 2023-05-10 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_estudiantee_delete_estudiante'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='estudiantee',
            new_name='estudiante',
        ),
    ]