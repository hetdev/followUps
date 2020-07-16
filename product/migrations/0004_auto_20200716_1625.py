# Generated by Django 3.0.8 on 2020-07-16 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='tariff',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]