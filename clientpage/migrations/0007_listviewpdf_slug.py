# Generated by Django 3.1.3 on 2021-04-28 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientpage', '0006_listviewpdf_is_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='listviewpdf',
            name='slug',
            field=models.SlugField(auto_created=True, default=1, unique=True),
            preserve_default=False,
        ),
    ]
