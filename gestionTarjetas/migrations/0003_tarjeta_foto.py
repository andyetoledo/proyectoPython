# Generated by Django 3.2.5 on 2021-12-09 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionTarjetas', '0002_alter_comentarios_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarjeta',
            name='foto',
            field=models.ImageField(null=True, upload_to='imgTarjetas'),
        ),
    ]
