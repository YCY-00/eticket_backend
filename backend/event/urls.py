from django.urls import path
from .views import (
    GetEventView,
    GetEventsView,
    GetParticipantsView,
    RegisterEventView,
    UpdateEventView,
    DeleteEventView,
)

app_name = "event"
urlpatterns = [
    path("event/<str:event_id>/", GetEventView.as_view()),
    path("events/", GetEventsView.as_view()),
    path("participants/<str:event_id>/", GetParticipantsView.as_view()),
    path("register/", RegisterEventView.as_view()),
    path("update/<str:event_id>/", UpdateEventView.as_view()),
    path("delete/<str:event_id>/", DeleteEventView.as_view()),
]
