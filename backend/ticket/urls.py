# urls.py
from django.urls import path
from .views import (
    get_ticket,
    get_tickets,
    register_ticket,
    update_ticket,
    delete_ticket,
)


app_name = "ticket"

urlpatterns = [
    path("register_ticket/", register_ticket, name="register_ticket"),
    path("update/<str:ticket_id>", update_ticket, name="update_ticket"),
    path("get/<str:ticket_id>/", get_event, name="get_event"),
    path("get/", get_tickets, name="get_tickets"),
    path("delete/<str:ticket_id>", delete_ticket, name="delete_ticket"),
]
