# Generated by Django 3.0.6 on 2020-05-16 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]