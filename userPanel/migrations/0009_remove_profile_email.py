# Generated by Django 3.2.2 on 2021-05-15 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userPanel', '0008_auto_20201201_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
