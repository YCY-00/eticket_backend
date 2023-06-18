from django.urls import path
from .views import (
    get_notification
    get_notifications,
    register_notificaiton,
    update_notificaiton,
    delete_notification,
)


app_name = "notification"

urlpatterns = [
    path("register_notificaiton/", register_notification, name="register_notification"),
    path("update/<str:notification_id>", update_notification, name="update_notification"),
    path("get/<str:notification_id>/", get_notification, name="get_notification"),
    path("get/", get_notificaitons, name="get_notifications"),
    path("delete/<str:notification_id>", delete_notification, name="delete_notification"),
]
