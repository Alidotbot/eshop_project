# Generated by Django 4.1 on 2022-12-10 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0006_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='آدرس'),
        ),
    ]