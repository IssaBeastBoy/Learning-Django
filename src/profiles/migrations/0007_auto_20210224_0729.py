# Generated by Django 3.1.6 on 2021-02-24 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20210223_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
    ]
