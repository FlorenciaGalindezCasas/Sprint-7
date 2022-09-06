# Generated by Django 4.1 on 2022-09-06 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Clientes", "0003_remove_cliente_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="customer_name",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="customer_surname",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="direccioncliente",
            name="ciudad",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="direccioncliente",
            name="direccion",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="direccioncliente",
            name="pais",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="direccioncliente",
            name="provincia",
            field=models.CharField(max_length=30),
        ),
    ]
