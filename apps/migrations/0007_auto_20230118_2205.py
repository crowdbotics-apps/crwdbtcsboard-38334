# Generated by Django 2.2.28 on 2023-01-18 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_auto_20230118_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='description',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='application',
            name='domain_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='framework',
            field=models.CharField(choices=[('DJANGO', 'Django'), ('REACT', 'React')], default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='type',
            field=models.CharField(choices=[('WEB', 'Web'), ('MOBILE', 'Mobile')], default='None', max_length=50),
        ),
    ]
