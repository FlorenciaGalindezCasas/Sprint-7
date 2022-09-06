# Generated by Django 4.1 on 2022-09-06 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Tarjetas", "0002_tarjetas_user_alter_tarjetas_cvv_and_more"),
        ("Prestamos", "0005_prestamo_branch_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("registration", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usuario",
            name="email",
        ),
        migrations.RemoveField(
            model_name="usuario",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="usuario",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="usuario",
            name="username",
        ),
        migrations.AddField(
            model_name="usuario",
            name="prestamos",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="Prestamos.prestamo",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usuario",
            name="tarjetas",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="Tarjetas.tarjetas",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usuario",
            name="user",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
