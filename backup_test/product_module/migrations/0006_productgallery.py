# Generated by Django 4.1 on 2022-12-22 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0005_productvisit'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/product_gallery', verbose_name='تصویر محصول')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'تصویر محصول',
                'verbose_name_plural': 'تصاویر محصول',
            },
        ),
    ]