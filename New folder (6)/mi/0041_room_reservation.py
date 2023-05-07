# Generated by Django 4.1.5 on 2023-03-13 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0040_alter_booking_booked_on_alter_booking_room_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='اسم اتاق')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='قیمت')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone_number', models.CharField(max_length=20, verbose_name='تلفن همراه')),
                ('check_in_date', models.DateField(verbose_name='تاریخ ورود')),
                ('check_out_date', models.DateField(verbose_name='تاریخ خروج')),
                ('number_of_guests', models.IntegerField(verbose_name='تعداد مهمان ها')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_module.room', verbose_name='اتاق')),
            ],
        ),
    ]