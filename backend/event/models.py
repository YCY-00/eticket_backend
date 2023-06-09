import uuid

from django.db import models

from backend.users.models import User

# Create your models here.
class EventModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=1000)
    date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=1000)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    capacity = models.IntegerField()
    remaining_capacity = models.IntegerField()

    def __str__(self):
        return self.title

    def decrement_capacity(self):
        self.remaining_capacity -= 1
        self.save()
