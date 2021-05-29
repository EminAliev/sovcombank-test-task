# Generated by Django 3.2.3 on 2021-05-29 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('changelog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='changelog',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор изменения'),
        ),
    ]
