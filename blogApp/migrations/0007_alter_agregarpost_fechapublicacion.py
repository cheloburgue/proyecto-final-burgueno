# Generated by Django 4.2.4 on 2023-10-03 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0006_alter_agregarpost_fechapublicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agregarpost',
            name='fechaPublicacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]