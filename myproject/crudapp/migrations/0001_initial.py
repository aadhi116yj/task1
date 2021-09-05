# Generated by Django 3.2 on 2021-08-14 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=50)),
                ('sroll', models.IntegerField(max_length=50)),
                ('sbranch', models.IntegerField(max_length=50)),
                ('semail', models.EmailField(max_length=50)),
                ('smobail', models.EmailField(max_length=254)),
            ],
        ),
    ]