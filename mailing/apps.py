from django.apps import AppConfig


class MailingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mailing"
    verbose_name = "Рассылки"

    # def ready(self):
    #     from mailing.services import start_send_mailing
    #     start_send_mailing()
