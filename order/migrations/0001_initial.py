# Generated by Django 3.0.8 on 2020-07-16 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('number', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField()),
                ('activation_date', models.DateField()),
                ('observations', models.CharField(blank=True, max_length=400, null=True)),
                ('project', models.CharField(max_length=200)),
                ('months', models.SmallIntegerField()),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=23)),
                ('vat', models.DecimalField(decimal_places=2, max_digits=23)),
                ('total', models.DecimalField(decimal_places=2, max_digits=23)),
                ('commercial_code', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]