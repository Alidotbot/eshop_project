# Generated by Django 4.1 on 2022-12-22 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0007_remove_productgallery_image_productgallery_image1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productgallery',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='productgallery',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='productgallery',
            name='image3',
        ),
        migrations.AddField(
            model_name='productgallery',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/product_gallery', verbose_name='تصویر محصول'),
        ),
    ]
