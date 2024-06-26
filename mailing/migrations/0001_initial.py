# Generated by Django 4.0 on 2024-06-16 18:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['email'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='Тема сообщения')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Тело сообщения')),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письма',
                'ordering': ['subject'],
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название рассылки')),
                ('start_mailing', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и время начала рассылки')),
                ('period', models.CharField(choices=[('раз в день', 'раз в день'), ('раз в неделю', 'раз в неделю'), ('раз в месяц', 'раз в месяц')], max_length=15, verbose_name='Периодичность рассылки')),
                ('status_mailing', models.CharField(choices=[('создана', 'создана'), ('завершена', 'завершена'), ('запущена', 'запущена')], max_length=10, verbose_name='Статус рассылки')),
                ('clients', models.ManyToManyField(help_text='Укажите клиентов сервиса', to='mailing.Client', verbose_name='Клиенты сервиса')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.message', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='LoggingMailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_attempt_mailing', models.DateTimeField(auto_now=True, verbose_name='Дата и время последней попытки')),
                ('status_attempt', models.BooleanField(choices=[('успешно', 'успешно'), ('неуспешно', 'неуспешно')], max_length=10, verbose_name='Статус попытки')),
                ('response', models.TextField(blank=True, null=True, verbose_name='Ответ сервера')),
                ('mailing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mailing.mailing', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Логирование',
                'verbose_name_plural': 'Логирование',
            },
        ),
    ]
