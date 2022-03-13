from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Chat(models.Model):
    '''Сущность чата'''
    chat_name = models.CharField(verbose_name='Название чата', max_length=255)
    members = models.ManyToManyField(User, verbose_name="Участники")
    messages = models.ManyToManyField('Message_chat', verbose_name="Сообщения", null=True, blank=True,
                                      related_name='messages_from_this_chat')
    last_message = models.ForeignKey('Message_chat', on_delete=models.CASCADE, verbose_name="Последнее сообщение",
                                     related_name='last_message_chat', null=True, blank=True)

    def __str__(self):
        return f'Чат : {self.chat_name}, {self.id}'

    class Meta:
        verbose_name = _("Чаты")
        verbose_name_plural = _("Чаты")


class Message_chat(models.Model):
    '''Сообщения чата'''
    chat = models.ForeignKey(Chat, verbose_name="Чат", on_delete=models.CASCADE, related_name='chat')
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    type = models.TextField(verbose_name='Тип сообщения')
    message = models.TextField(verbose_name="Текст сообщения", null=True, blank=True)
    pub_date = models.DateTimeField('Дата создания', auto_now_add=True)
    is_readed = models.BooleanField('Прочитано?', default=False)

    class Meta:
        ordering = ['pub_date']
        verbose_name = _("Сообщения")
        verbose_name_plural = _("Сообщения")

    def __str__(self):
        return f'{self.author} : {self.message}'
