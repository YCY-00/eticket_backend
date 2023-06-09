from django.contrib import admin

from backend.notification.models import NotificationModel


@admin.register(NotificationModel)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'user', 'created_at', 'updated_at')
    list_filter = ('user', 'created_at', 'updated_at')
    search_fields = ('title', 'message', 'user')
    ordering = ('created_at', 'updated_at')
