# Generated by Django 3.0.8 on 2020-07-16 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=200)),
                ('public_name', models.CharField(max_length=200)),
                ('nit', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=200)),
                ('contact_name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('billing_email', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
            ],
        ),
    ]
