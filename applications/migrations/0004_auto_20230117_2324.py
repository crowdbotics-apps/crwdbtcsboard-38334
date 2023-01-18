# Generated by Django 2.2.28 on 2023-01-17 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_auto_20230117_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='application_subscription', to='subscriptions.Subscription'),
        ),
    ]