# Generated by Django 2.0.13 on 2019-05-07 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebVentaLibros', '0005_libro_cantidad_libro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='titulo_libro',
        ),
    ]
