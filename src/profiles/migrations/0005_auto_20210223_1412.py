# Generated by Django 3.1.6 on 2021-02-23 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20210223_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Applications',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Field',
            field=models.CharField(max_length=50),
        ),
    ]