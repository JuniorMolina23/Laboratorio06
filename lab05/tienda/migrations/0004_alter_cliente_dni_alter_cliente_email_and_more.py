# Generated by Django 4.1.1 on 2022-09-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=10),
        ),
    ]
