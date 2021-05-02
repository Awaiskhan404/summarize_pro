# Generated by Django 3.1.3 on 2021-04-27 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListViewPdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdffile', models.FileField(upload_to='')),
                ('is_paid', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
                ('number_pages', models.TextField(blank=True)),
            ],
        ),
    ]