# Generated by Django 4.1.5 on 2023-03-12 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0008_initial'),
        ('home_module', '0037_remove_contact_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_module.admin', verbose_name='توسط ادمین'),
        ),
    ]
