from django.urls import path, include

from . import views

urlpatterns = [
    path("inbox/", views.inbox, name="inbox"),
    path("send/", views.send_message, name="send_message"),
    path("inbox/<int:message_id>/", views.detail, name="detail"),
]