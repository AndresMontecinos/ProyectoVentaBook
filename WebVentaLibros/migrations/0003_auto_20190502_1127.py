# Generated by Django 2.0.13 on 2019-05-02 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebVentaLibros', '0002_auto_20190501_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_libro', models.IntegerField()),
                ('titulo_libro', models.CharField(max_length=50)),
                ('autor_libro', models.CharField(max_length=50)),
                ('eiditorial_libro', models.CharField(max_length=50)),
                ('descripcion_libro', models.TextField(max_length=180)),
                ('precio_libro', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='producto',
        ),
    ]
