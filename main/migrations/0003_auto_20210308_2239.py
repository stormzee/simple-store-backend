# Generated by Django 3.1.7 on 2021-03-08 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210308_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_amount',
            field=models.FloatField(default=0),
        ),
    ]
