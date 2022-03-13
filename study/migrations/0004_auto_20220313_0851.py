# Generated by Django 3.2.4 on 2022-03-13 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_auto_20220313_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='publications',
            field=models.ManyToManyField(blank=True, null=True, related_name='publications_1', to='study.Publications', verbose_name='Публикации'),
        ),
        migrations.AddField(
            model_name='student',
            name='publications',
            field=models.ManyToManyField(blank=True, null=True, related_name='publications_2', to='study.Publications', verbose_name='Публикации'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='publications',
            field=models.ManyToManyField(blank=True, null=True, related_name='publications_3', to='study.Publications', verbose_name='Публикации'),
        ),
    ]