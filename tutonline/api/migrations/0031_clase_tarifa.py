# Generated by Django 4.2.1 on 2023-05-15 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_claseagendada'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='tarifa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
