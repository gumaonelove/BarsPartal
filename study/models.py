from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

User = settings.AUTH_USER_MODEL


class Subject(models.Model):
    '''Предмет изучения'''
    name = models.CharField(verbose_name='Название предмета', max_length=100, unique=True)

    def __str__(self):
        return f'Предмет: {self.name}'

    class Meta:
        verbose_name = _("Предметы")
        verbose_name_plural = _("Предметы")


class Student(models.Model):
    '''Ребенок'''

    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.SET_NULL, null=True, blank=True, related_name='student_user')
    surname = models.CharField(verbose_name='Фамилия', max_length=30, null=True)
    name = models.CharField(verbose_name='Имя', max_length=30, null=True)
    lastname = models.CharField(verbose_name='Отчество', max_length=30, null=True)
    image = models.ImageField(verbose_name='Фотографии', null=True, blank=True)

    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True)

    publications = models.ManyToManyField(
        'Publications', verbose_name='Публикации', related_name='publications_2', null=True, blank=True)

    events = models.ManyToManyField('Event', verbose_name='Мероприятия', null=True, blank=True)

    def get_full_name(self):
        if self.surname:
            return self.surname + ' ' + self.name + ' ' + self.lastname

    achievements = models.ManyToManyField(
        'Achievements', verbose_name='Портфолио', null=True, blank=True)

    school_class = models.CharField(verbose_name='Школьный класс', max_length=50)
    rang = models.IntegerField(verbose_name='Рейтинг', null=True, blank=True)

    def __str__(self):
        return f'Ученик: {self.get_full_name()}'

    class Meta:
        verbose_name = _("Ученики")
        verbose_name_plural = _("Ученики")


class Parent(models.Model):
    '''Родитель'''

    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.SET_NULL, null=True, blank=True)
    surname = models.CharField(verbose_name='Фамилия', max_length=30, null=True)
    name = models.CharField(verbose_name='Имя', max_length=30, null=True)
    lastname = models.CharField(verbose_name='Отчество', max_length=30, null=True)
    image = models.ImageField(verbose_name='Фотографии', null=True, blank=True)

    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True)

    publications = models.ManyToManyField(
        'Publications', verbose_name='Публикации', related_name='publications_1', null=True, blank=True)
    events = models.ManyToManyField('Event', verbose_name='Мероприятия', null=True, blank=True)

    def get_full_name(self):
        if self.surname:
            return self.surname + ' ' + self.name + ' ' + self.lastname

    child = models.ManyToManyField(Student, verbose_name="Дети")

    def __str__(self):
        return f'Родитель: {self.get_full_name()}'

    class Meta:
        verbose_name = _("Родители")
        verbose_name_plural = _("Родители")


class Teacher(models.Model):
    '''Учитель'''
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.SET_NULL, null=True, blank=True)
    surname = models.CharField(verbose_name='Фамилия', max_length=30, null=True)
    name = models.CharField(verbose_name='Имя', max_length=30, null=True)
    lastname = models.CharField(verbose_name='Отчество', max_length=30, null=True)
    image = models.ImageField(verbose_name='Фотографии', null=True, blank=True)

    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True)

    publications = models.ManyToManyField(
        'Publications', verbose_name='Публикации', related_name='publications_3', null=True, blank=True)
    events = models.ManyToManyField('Event', verbose_name='Мероприятия', null=True, blank=True)

    def get_full_name(self):
        if self.surname:
            return self.surname + ' ' + self.name + ' ' + self.lastname

    achievements = models.ManyToManyField(
        'Achievements', verbose_name='Портфолио', null=True, blank=True)

    subject = models.ForeignKey(Subject, verbose_name='Предмет', on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(verbose_name="Описание")

    is_tutor = models.BooleanField(verbose_name='Репетитор?')
    rang = models.IntegerField(verbose_name='Рейтинг', null=True, blank=True)

    def __str__(self):
        return f'Учитель: {self.get_full_name()}'


    class Meta:
        verbose_name = _("Учителя")
        verbose_name_plural = _("Учителя")


class Achievements(models.Model):
    '''Достижения'''
    title = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото')

    def __str__(self):
        return f'Достижение: {self.title}'

    class Meta:
        verbose_name = _("Достижения")
        verbose_name_plural = _("Достижения")


class Event(models.Model):
    '''Мероприятие'''
    title = models.TextField(verbose_name='Название мероприятия')
    peoples = models.ManyToManyField(User, verbose_name='Участники мероприятия')
    active = models.BooleanField(verbose_name="Активное?")
    text = models.TextField(verbose_name='Описание')

    created_at = models.DateTimeField(verbose_name='Создана', auto_now_add=True)

    def __str__(self):
        return f'Мероприятие: {self.title}'

    class Meta:
        verbose_name = _("Мероприятия")
        verbose_name_plural =_("Мероприятия")


class Publications(models.Model):
    '''Публикации'''
    author = models.ForeignKey(User, verbose_name='Авторы публикации', related_name='author_publications', on_delete=models.CASCADE)
    title = models.TextField(verbose_name='Название публикации')
    text = models.TextField(verbose_name='Текст публикации')
    image = models.ImageField(verbose_name='Изображения')

    created_at = models.DateTimeField(verbose_name='Создана', auto_now_add=True)

    def __str__(self):
        return f'Публикация: {self.title}'

    class Meta:
        verbose_name = _("Публикации")
        verbose_name_plural =_("Публикации")
