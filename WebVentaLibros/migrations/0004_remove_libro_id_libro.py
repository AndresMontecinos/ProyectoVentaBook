# Generated by Django 2.0.13 on 2019-05-02 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebVentaLibros', '0003_auto_20190502_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='id_libro',
        ),
    ]