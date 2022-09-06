# Generated by Django 4.1 on 2022-09-06 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Cuentas", "0003_remove_cuenta_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cuenta",
            name="iban",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="cuenta",
            name="tipo_cuenta",
            field=models.CharField(default="Classic", max_length=20),
        ),
    ]
