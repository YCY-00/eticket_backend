# urls.py
from django.urls import path
from .views import (
    register_event,
    update_event,
    get_event,
    get_events,
    delete_event,
    get_participants,
)

app_name = "event"

urlpatterns = [
    path("register/", register_event, name="register_event"),
    path("update/<str:event_id>", update_event, name="update_event"),
    path("get/<str:event_id>/", get_event, name="get_event"),
    path("get/", get_events, name="get_events"),
    path("delete/<str:event_id>", delete_event, name="delete_event"),
    path("get_participants/<str:event_id>/", get_participants, name="get_participants"),
]
