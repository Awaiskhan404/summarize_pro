# Generated by Django 3.1.3 on 2021-04-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ifpaid',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pdf',
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
