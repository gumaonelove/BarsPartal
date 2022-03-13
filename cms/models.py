from django.db import models
from django.utils.translation import ugettext_lazy as _


class Image(models.Model):
    '''Изображение'''
    image = models.ImageField(verbose_name='Изображение')

    def __str__(self):
        return f'Изображение: {self.id}'

    class Meta:
        verbose_name = _("Изображения")
        verbose_name_plural = _("Изображения")


class File(models.Model):
    '''Файл'''
    file = models.FileField(verbose_name='Файл')

    def __str__(self):
        return f'Файл: {self.id}'

    class Meta:
        verbose_name = _("Файлы")
        verbose_name_plural = _("Файлы")


class Developer(models.Model):
    '''Команда'''
    name = models.CharField(verbose_name='Имя', max_length=30)
    surname = models.CharField(verbose_name='Фамилия', max_length=30)
    image = models.ImageField(verbose_name='Фотография')

    position = models.CharField(verbose_name='Должность', max_length=50)

    def get_name(self):
        return self.surname + ' ' + self.name

    def __str__(self):
        return f'{self.position} - {self.name}'

    class Meta:
        verbose_name = _("Разработчики")
        verbose_name_plural = _("Разработчики")
