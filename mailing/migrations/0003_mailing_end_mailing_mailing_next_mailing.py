# Generated by Django 4.2.7 on 2024-06-22 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_alter_loggingmailing_status_attempt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='end_mailing',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время последней отправки рассылки'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='next_mailing',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время следующей отправки рассылки'),
        ),
    ]
