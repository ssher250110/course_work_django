from django.conf import settings
from django.db import models
from django.utils import timezone

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):
    """Модель клиента"""
    email = models.EmailField(unique=True, verbose_name="Почта")
    last_name = models.CharField(max_length=50, **NULLABLE, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, **NULLABLE, verbose_name="Имя")
    middle_name = models.CharField(max_length=50, **NULLABLE, verbose_name="Отчество")
    comment = models.TextField(**NULLABLE, verbose_name="Комментарий")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return (f"Почта: {self.email} "
                f"Фамилия: {self.last_name if self.last_name else "Отсутствует"} "
                f"Имя: {self.first_name if self.first_name else "Отсутствует"} "
                f"Отчество: {self.middle_name if self.middle_name else "Отсутствует"} "
                f"Комментарий: {self.comment if self.comment else "Отсутствует"} ")

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["email", ]


class Message(models.Model):
    """Модель сообщения"""
    subject = models.CharField(max_length=255, verbose_name="Тема сообщения")
    body = models.TextField(**NULLABLE, verbose_name="Тело сообщения")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return f"{self.subject}: {self.body}"

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"
        ordering = ["subject", ]


class Mailing(models.Model):
    """Модель рассылки"""
    PERIOD = [
        ("раз в день", "раз в день"),
        ("раз в неделю", "раз в неделю"),
        ("раз в месяц", "раз в месяц"),
    ]
    STATUS = [
        ("создана", "создана"),
        ("запущена", "запущена"),
    ]
    name = models.CharField(unique=True, max_length=255, verbose_name="Название рассылки")
    clients = models.ManyToManyField("Client", verbose_name="Клиенты")
    message = models.ForeignKey("Message", on_delete=models.CASCADE, verbose_name="Сообщение")
    start_mailing = models.DateTimeField(default=timezone.now, verbose_name="Дата и время первой отправки рассылки")
    period = models.CharField(max_length=15, choices=PERIOD, verbose_name="Периодичность рассылки")
    status_mailing = models.CharField(default="создана", max_length=10, choices=STATUS, verbose_name="Статус рассылки")
    is_active = models.BooleanField(default=True, verbose_name="Активная рассылка")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')

    def __str__(self):
        return f"{self.name}, start: {self.start_mailing}, status:{self.status_mailing}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["name", ]


class LoggingMailing(models.Model):
    """Модель лога"""
    mailing = models.ForeignKey("Mailing", on_delete=models.CASCADE, **NULLABLE, verbose_name="Рассылка")
    last_attempt_mailing = models.DateTimeField(auto_now=True, verbose_name="Дата и время последней попытки")
    status_attempt = models.BooleanField(max_length=10, default=False, verbose_name="Статус попытки")
    response = models.TextField(**NULLABLE, verbose_name='Ответ сервера')

    def __str__(self):
        return (f"{self.mailing}: Дата и время последней попытки({self.last_attempt_mailing})\n"
                f"Статус попытки{self.status_attempt}\n"
                f"Ответ сервера{self.response}")

    class Meta:
        verbose_name = 'Логирование'
        verbose_name_plural = 'Логирование'
