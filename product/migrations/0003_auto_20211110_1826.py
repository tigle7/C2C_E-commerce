# Generated by Django 3.2.9 on 2021-11-10 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='uploads', verbose_name='Picture'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]