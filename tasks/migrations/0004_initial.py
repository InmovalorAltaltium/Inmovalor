# Generated by Django 5.2.1 on 2025-05-31 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0003_delete_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlcaldiaVista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado', models.CharField(max_length=100)),
                ('Alcaldia', models.CharField(max_length=100)),
                ('Colonia', models.CharField(max_length=100)),
                ('Promedio_MXN', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Zona', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'alcaldia_vistas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_postal', models.CharField(max_length=5)),
                ('colonia', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('calle', models.CharField(max_length=100)),
                ('tipo_propiedad', models.CharField(max_length=50)),
                ('recamaras', models.IntegerField()),
                ('sanitarios', models.DecimalField(decimal_places=1, max_digits=3)),
                ('estacionamiento', models.IntegerField()),
                ('terreno', models.DecimalField(decimal_places=2, max_digits=10)),
                ('construccion', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado_conservacion', models.CharField(max_length=50)),
                ('comentarios', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
