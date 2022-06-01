# Generated by Django 3.1.7 on 2022-01-27 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoModel',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('codigo', models.BigIntegerField(db_column='codigo')),
                ('descripcion', models.CharField(db_column='descripcion', max_length=300)),
                ('detalle_producto', models.CharField(db_column='detalle_producto', max_length=300)),
                ('talla', models.CharField(db_column='talla', max_length=100)),
                ('precio_unitario', models.BigIntegerField(blank=True, db_column='precio_unitario')),
                ('valor', models.BigIntegerField(db_column='valor')),
                ('valor_venta', models.BigIntegerField(db_column='valor_venta')),
                ('descuento', models.FloatField(db_column='descuento')),
                ('cantidad', models.IntegerField(blank=True, db_column='cantidad')),
                ('valor_descuento', models.BigIntegerField(db_column='valor_descuento')),
                ('id_motivo', models.IntegerField(choices=[('1', 'Niño'), ('2', 'Niña')], db_column='id_motivo')),
                ('referencia', models.IntegerField(db_column='referencia', unique=True)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True, db_column='fecha_ingreso')),
                ('pieza', models.IntegerField(db_column='pieza')),
            ],
            options={
                'verbose_name': 'Productos',
                'verbose_name_plural': 'productos',
                'db_table': 'producto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImagenProductoModel',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(db_column='descripcion', max_length=300)),
                ('adjunto', models.FileField(blank=True, db_column='adjunto', default=None, null=True, upload_to='img/producto/')),
                ('producto', models.ForeignKey(db_column='id_producto', on_delete=django.db.models.deletion.CASCADE, to='producto.productomodel')),
            ],
            options={
                'verbose_name': 'imagen-producto',
                'verbose_name_plural': 'imagenes-productos',
                'db_table': 'imagen-producto',
                'managed': True,
            },
        ),
    ]