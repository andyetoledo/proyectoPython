# Generated by Django 3.2.5 on 2021-11-22 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionTarjetas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='comentario',
            field=models.CharField(max_length=250),
        ),
    ]