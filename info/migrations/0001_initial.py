# Generated by Django 3.2.4 on 2022-03-13 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
            ],
            options={
                'verbose_name': 'Электронная почта',
                'verbose_name_plural': 'Электронная почта',
            },
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Номер телефона',
                'verbose_name_plural': 'Номер телефона',
            },
        ),
    ]