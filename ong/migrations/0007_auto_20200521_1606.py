# Generated by Django 3.0.6 on 2020-05-21 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0006_auto_20200518_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
