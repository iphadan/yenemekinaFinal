# Generated by Django 5.0 on 2024-04-10 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_post_car_alter_yeneuser_user_carimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
