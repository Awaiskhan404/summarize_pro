# Generated by Django 3.1.3 on 2021-04-24 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210424_1152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='infos_pdf',
            new_name='bio',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pdf_file',
        ),
    ]