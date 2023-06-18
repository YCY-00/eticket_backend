from django.urls import path
from .views import (
    GetNotificationView,
    GetNotificationsView,
    RegisterNotificationView,
    UpdateNotificationView,
    DeleteNotificationView,
)

app_name = "notification"
urlpatterns = [
    path("notification/<str:notification_id>/", GetNotificationView.as_view()),
    path("notifications/", GetNotificationsView.as_view()),
    path("register/", RegisterNotificationView.as_view()),
    path("update/<str:notification_id>/", UpdateNotificationView.as_view()),
    path("delete/<str:notification_id>/", DeleteNotificationView.as_view()),
]
