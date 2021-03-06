# Generated by Django 3.2.4 on 2022-03-13 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_auto_20220313_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='images',
        ),
        migrations.RemoveField(
            model_name='student',
            name='images',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='images',
        ),
        migrations.AddField(
            model_name='parent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотографии'),
        ),
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотографии'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотографии'),
        ),
    ]
