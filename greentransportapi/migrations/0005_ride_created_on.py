# Generated by Django 4.1.3 on 2024-08-07 00:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('greentransportapi', '0004_maintenancepart'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
