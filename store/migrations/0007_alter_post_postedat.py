# Generated by Django 5.0 on 2024-04-18 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_car_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postedAt',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 18, 14, 13, 19, 933627)),
        ),
    ]
