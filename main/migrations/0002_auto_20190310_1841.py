# Generated by Django 2.1.6 on 2019-03-10 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerDetails',
            fields=[
                ('hostname', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='servers',
            old_name='name',
            new_name='hostname',
        ),
    ]