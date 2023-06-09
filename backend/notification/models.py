from django.db import models

from backend.users.models import User

# Create your models here.
class NotificationModel(models.Model):

    title = models.CharField(max_length=1000)
    message = models.CharField(max_length=1000)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')

    def __str__(self):
        return self.title
