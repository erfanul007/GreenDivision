# Generated by Django 3.1.1 on 2020-09-27 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=300)),
                ('url', models.URLField(max_length=100, unique=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModelName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('varsity_id', models.CharField(max_length=100, unique=True)),
                ('uri_link', models.URLField(max_length=100, unique=True)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('show_email', models.BooleanField(default=False)),
                ('show_number', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
