# Generated by Django 5.0.7 on 2024-08-01 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]
