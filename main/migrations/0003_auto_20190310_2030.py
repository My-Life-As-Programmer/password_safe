# Generated by Django 2.1.6 on 2019-03-10 15:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190310_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverdetails',
            name='last_password',
            field=models.CharField(default='hi', max_length=50),
        ),
        migrations.AddField(
            model_name='serverdetails',
            name='last_password_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='serverdetails',
            name='password',
            field=models.CharField(default='hi', max_length=50),
        ),
    ]
