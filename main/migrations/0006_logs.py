# Generated by Django 2.2.1 on 2019-05-21 11:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190311_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serv_name', models.CharField(max_length=50)),
                ('user_accessed', models.CharField(max_length=50)),
                ('time_of_access', models.DateTimeField(default=django.utils.timezone.now)),
                ('reason', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'ServerDetails',
            },
        ),
    ]
