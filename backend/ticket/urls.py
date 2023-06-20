from django.urls import path
from .views import (
    GetEventTicketsView,
    GetTicketView,
    GetTicketsView,
    RegisterTicketView,
    UpdateTicketView,
    DeleteTicketView,
)


app_name = "ticket"
urlpatterns = [
    path("ticket/<str:ticket_id>/", GetTicketView.as_view()),
    path("event/<str:event_id>/", GetEventTicketsView.as_view()),
    path("ticket/<str:ticket_id>/", GetTicketView.as_view()),
    path("tickets/", GetTicketsView.as_view()),
    path("register/", RegisterTicketView.as_view()),
    path("update/<str:ticket_id>/", UpdateTicketView.as_view()),
    path("delete/<str:ticket_id>/", DeleteTicketView.as_view()),
]
