# Generated by Django 3.2.4 on 2022-03-13 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Достижения',
                'verbose_name_plural': 'Достижения',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Название мероприятия')),
                ('active', models.BooleanField(verbose_name='Активное?')),
                ('text', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создана')),
                ('peoples', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Участники мероприятия')),
            ],
            options={
                'verbose_name': 'Мероприятия',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название предмета')),
            ],
            options={
                'verbose_name': 'Предметы',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30, null=True, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=30, null=True, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=30, null=True, verbose_name='Отчество')),
                ('position', models.CharField(choices=[('Ученик', 'Ученик'), ('Родитель', 'Родитель'), ('Учитель', 'Учитель')], max_length=15, null=True, verbose_name='Роль')),
                ('date_of_birth', models.DateField(null=True, verbose_name='Дата рождения')),
                ('text', models.IntegerField(verbose_name='Описание')),
                ('is_tutor', models.BooleanField(verbose_name='Репетитор?')),
                ('rang', models.IntegerField(blank=True, null=True, verbose_name='Рейтинг')),
                ('achievements', models.ManyToManyField(blank=True, null=True, to='study.Achievements', verbose_name='Портфолио')),
                ('events', models.ManyToManyField(blank=True, null=True, to='study.Event', verbose_name='Мероприятия')),
                ('images', models.ManyToManyField(blank=True, null=True, to='cms.Image', verbose_name='Фотографии')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='study.subject', verbose_name='Предмет')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Учителя',
                'verbose_name_plural': 'Учителя',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30, null=True, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=30, null=True, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=30, null=True, verbose_name='Отчество')),
                ('position', models.CharField(choices=[('Ученик', 'Ученик'), ('Родитель', 'Родитель'), ('Учитель', 'Учитель')], max_length=15, null=True, verbose_name='Роль')),
                ('date_of_birth', models.DateField(null=True, verbose_name='Дата рождения')),
                ('school_class', models.CharField(max_length=50, verbose_name='Школьный класс')),
                ('rang', models.IntegerField(blank=True, null=True, verbose_name='Рейтинг')),
                ('achievements', models.ManyToManyField(blank=True, null=True, to='study.Achievements', verbose_name='Портфолио')),
                ('events', models.ManyToManyField(blank=True, null=True, to='study.Event', verbose_name='Мероприятия')),
                ('images', models.ManyToManyField(blank=True, null=True, to='cms.Image', verbose_name='Фотографии')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Ученики',
                'verbose_name_plural': 'Ученики',
            },
        ),
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Название публикации')),
                ('text', models.TextField(verbose_name='Текст публикации')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создана')),
                ('author', models.ManyToManyField(related_name='author_publications', to=settings.AUTH_USER_MODEL, verbose_name='Авторы публикации')),
                ('files', models.ManyToManyField(to='cms.File', verbose_name='Файлы')),
                ('images', models.ManyToManyField(to='cms.Image', verbose_name='Изображения')),
            ],
            options={
                'verbose_name': 'Публикации',
                'verbose_name_plural': 'Публикации',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30, null=True, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=30, null=True, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=30, null=True, verbose_name='Отчество')),
                ('position', models.CharField(choices=[('Ученик', 'Ученик'), ('Родитель', 'Родитель'), ('Учитель', 'Учитель')], max_length=15, null=True, verbose_name='Роль')),
                ('date_of_birth', models.DateField(null=True, verbose_name='Дата рождения')),
                ('child', models.ManyToManyField(to='study.Student', verbose_name='Дети')),
                ('events', models.ManyToManyField(blank=True, null=True, to='study.Event', verbose_name='Мероприятия')),
                ('images', models.ManyToManyField(blank=True, null=True, to='cms.Image', verbose_name='Фотографии')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Родители',
                'verbose_name_plural': 'Родители',
            },
        ),
    ]
