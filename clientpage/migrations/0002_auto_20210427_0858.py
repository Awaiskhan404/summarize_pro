# Generated by Django 3.1.3 on 2021-04-27 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listviewpdf',
            options={'ordering': ('-name',)},
        ),
        migrations.RemoveField(
            model_name='listviewpdf',
            name='number_pages',
        ),
        migrations.AddField(
            model_name='listviewpdf',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
