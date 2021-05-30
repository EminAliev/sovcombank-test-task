from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save, post_delete

from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler


class Data(ChangeloggableMixin, models.Model):
    PRODUCT_CHOICES = [
        ('', 'Выберите тип продукта'),
        ('car', 'Авто'),
        ('consumer', 'Потреб'),
        ('deposit', 'Залог'),
        ('mortgage', 'Ипотека'),
    ]
    SOLUTION_CHOICES = [
        ('', 'Решение по заявке'),
        ('approved', 'Одобрено'),
        ('denied', 'Отказано'),
        ('temp_denied', 'Временно отказано'),
    ]
    date = models.DateTimeField('Дата заявки', auto_now_add=True)
    product = models.CharField('Продукт', max_length=20, choices=PRODUCT_CHOICES)
    phone_number = models.CharField('Номер телефона', validators=[RegexValidator(
        regex='^[0-9]{10}$',
        message='Номер телефона должен быть в формате 9xxxxxxxxx'
    )],
                                    max_length=10,
                                    help_text='Номер телефона в формате 9xxxxxxxxx')
    solution = models.CharField('Решение', choices=SOLUTION_CHOICES, max_length=20, blank=True, null=True)
    comment = models.TextField('Комментарий', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор заявки')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.product


post_save.connect(journal_save_handler, sender=Data)
post_delete.connect(journal_delete_handler, sender=Data)
