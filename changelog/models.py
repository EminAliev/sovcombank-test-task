from django.conf import settings
from django.db import models
from django.db.models import JSONField

ACTION_CREATE = 'create'
ACTION_UPDATE = 'update'
ACTION_DELETE = 'delete'


class ChangeLog(models.Model):
    TYPE_ACTION_ON_MODEL = (
        (ACTION_CREATE, 'Создание'),
        (ACTION_UPDATE, 'Изменение'),
        (ACTION_DELETE, 'Удаление'),
    )
    changed = models.DateTimeField(auto_now=True, verbose_name=u'Дата/время изменения')
    model = models.CharField(max_length=255, verbose_name=u'Таблица', null=True)
    record_id = models.IntegerField(verbose_name=u'ID записи', null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=u'Автор изменения',
        on_delete=models.CASCADE, null=True)
    action_on_model = models.CharField(
        choices=TYPE_ACTION_ON_MODEL, max_length=50, verbose_name=u'Действие', null=True)
    data = JSONField(verbose_name=u'Изменяемые данные модели', default=dict)

    class Meta:
        ordering = ('changed',)
        verbose_name = 'Логи'
        verbose_name_plural = 'Логи'

    def __str__(self):
        return f'{self.id}'

    @classmethod
    def add(cls, instance, user, action_on_model, data, id=None):
        """Создание записи в журнале регистрации изменений"""
        log = ChangeLog.objects.get(id=id) if id else ChangeLog()
        log.model = instance.__class__.__name__
        log.record_id = instance.pk
        if user:
            log.user = user
        log.action_on_model = action_on_model
        log.data = data
        log.save()
        return log.pk
