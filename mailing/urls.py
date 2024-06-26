from django.urls import path
# from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView, \
    MessageCreateView, MessageListView, MessageDetailView, MessageUpdateView, MessageDeleteView, \
    MailingCreateView, MailingListView, MailingDetailView, MailingUpdateView, MailingDeleteView, \
    InfoListView, ManagerListView, switcher_user_active, switcher_mailing_active

app_name = MailingConfig.name

urlpatterns = [
    path("", InfoListView.as_view(), name="info-view"),

    path("client/create/", ClientCreateView.as_view(), name="client-create"),
    path("client/", ClientListView.as_view(), name="client-list"),
    path("client/<int:pk>/", ClientDetailView.as_view(), name="client-detail"),
    path("client/<int:pk>/update/", ClientUpdateView.as_view(), name="client-update"),
    path("client/<int:pk>/delete/", ClientDeleteView.as_view(), name="client-delete"),

    path("message/create/", MessageCreateView.as_view(), name="message-create"),
    path("message/", MessageListView.as_view(), name="message-list"),
    path("message/<int:pk>/", MessageDetailView.as_view(), name="message-detail"),
    path("message/<int:pk>/update/", MessageUpdateView.as_view(), name="message-update"),
    path("message/<int:pk>/delete/", MessageDeleteView.as_view(), name="message-delete"),

    path("mailing/create/", MailingCreateView.as_view(), name="mailing-create"),
    path("mailing/", MailingListView.as_view(), name="mailing-list"),
    path("mailing/<int:pk>/", MailingDetailView.as_view(), name="mailing-detail"),
    path("mailing/<int:pk>/update/", MailingUpdateView.as_view(), name="mailing-update"),
    path("mailing/<int:pk>/delete/", MailingDeleteView.as_view(), name="mailing-delete"),

    path("manager/", ManagerListView.as_view(), name="manager"),
    path("user_active/<int:pk>/", switcher_user_active, name="switcher_user_active"),

    path("mailing_active/<int:pk>/", switcher_mailing_active, name="switcher_mailing_active"),
]
