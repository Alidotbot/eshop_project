# Generated by Django 4.1.5 on 2023-03-11 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_module', '0007_delete_admin_delete_customer_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='نام')),
                ('email', models.CharField(max_length=500, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=300, verbose_name='تلفن همراه')),
                ('gender', models.CharField(max_length=300, verbose_name='جنسیت')),
            ],
            options={
                'verbose_name': 'ادمین',
                'verbose_name_plural': 'ادمین ها',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=300, verbose_name='نام')),
                ('password', models.CharField(max_length=300, verbose_name='رمز')),
                ('email', models.CharField(max_length=500, verbose_name='ایمیل')),
                ('profile_pic', models.ImageField(blank=True, upload_to='uploads', verbose_name='پروفایل')),
                ('phone_number', models.CharField(max_length=50, verbose_name='تلفن همراه')),
                ('address', models.CharField(max_length=500, verbose_name='ادرس')),
                ('pin_code', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'تنظیمات کاربر',
                'verbose_name_plural': 'تنظیمات کاربران',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, verbose_name='نام')),
                ('password', models.CharField(max_length=100, verbose_name='رمز')),
                ('email', models.CharField(max_length=500, verbose_name='ایمیل')),
                ('profile_pic', models.ImageField(blank=True, upload_to='uploads', verbose_name='پروفایل')),
                ('phone_number', models.CharField(max_length=50, verbose_name='تلفن همراه')),
                ('gender', models.CharField(max_length=50, verbose_name='جنسیت')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
    ]
