# Generated by Django 4.1.5 on 2023-03-12 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0036_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='admin',
        ),
    ]
