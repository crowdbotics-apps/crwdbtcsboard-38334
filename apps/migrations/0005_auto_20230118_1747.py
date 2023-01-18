# Generated by Django 2.2.28 on 2023-01-18 17:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_auto_20230118_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='description',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(1, 'the field must contain at least 1 characters')], verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='application',
            name='domain_name',
            field=models.CharField(max_length=50, verbose_name='Domain Name'),
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
    ]