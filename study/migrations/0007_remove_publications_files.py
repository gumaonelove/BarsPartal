# Generated by Django 3.2.4 on 2022-03-13 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0006_auto_20220313_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publications',
            name='files',
        ),
    ]
