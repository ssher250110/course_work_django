# Generated by Django 4.2.7 on 2024-06-23 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_alter_mailing_status_mailing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='end_mailing',
        ),
    ]
