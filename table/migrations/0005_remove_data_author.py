# Generated by Django 3.2.3 on 2021-05-30 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0004_data_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='author',
        ),
    ]
