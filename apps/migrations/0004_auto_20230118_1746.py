# Generated by Django 2.2.28 on 2023-01-18 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_auto_20230118_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='framework',
            field=models.CharField(choices=[('DJANGO', 'Django'), ('REACT', 'React Native')], default=None, max_length=50, verbose_name='Framework'),
        ),
    ]
