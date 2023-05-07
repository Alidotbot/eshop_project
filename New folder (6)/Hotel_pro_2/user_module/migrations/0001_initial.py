# Generated by Django 4.1.5 on 2023-02-02 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=300, verbose_name='')),
                ('password', models.CharField(max_length=300, verbose_name='')),
                ('email', models.CharField(max_length=500, verbose_name='')),
                ('profile_pic', models.ImageField(blank=True, upload_to='uploads', verbose_name='')),
                ('phone_number', models.CharField(max_length=50, verbose_name='')),
                ('address', models.CharField(max_length=500, verbose_name='')),
                ('pin_code', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, verbose_name='')),
                ('password', models.CharField(max_length=100, verbose_name='')),
                ('email', models.CharField(max_length=500, verbose_name='')),
                ('profile_pic', models.ImageField(blank=True, upload_to='uploads', verbose_name='')),
                ('phone_number', models.CharField(max_length=50, verbose_name='')),
                ('gender', models.CharField(max_length=50, verbose_name='')),
            ],
        ),
    ]