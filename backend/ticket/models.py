from django.db import models
import uuid

# Create your models here.
class TicketModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey('event.EventModel', on_delete=models.CASCADE, related_name='tickets')
    price = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

