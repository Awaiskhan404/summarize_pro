# Generated by Django 3.1.3 on 2021-04-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientpage', '0009_auto_20210428_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listviewpdf',
            name='total_price',
            field=models.FloatField(),
        ),
    ]
