from django.db import models
from django.utils.translation import ugettext_lazy as _


class PhoneNumber(models.Model):
    '''Номер телефона'''
    number = models.CharField(verbose_name='Номер телефона', max_length=15)

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = _("Номер телефона")
        verbose_name_plural = _("Номер телефона")


class Email(models.Model):
    '''Электронная почта'''
    email = models.EmailField(verbose_name='Электронная почта')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = _("Электронная почта")
        verbose_name_plural = _("Электронная почта")