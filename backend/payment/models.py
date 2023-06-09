from django.db import models
import uuid
from backend.ticket.models import TicketModel

from backend.users.models import User
# Create your models here.

class PaymentModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    ticket = models.ForeignKey(TicketModel, on_delete=models.CASCADE, related_name='payments')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    is_refunded = models.BooleanField(default=False)

    def __str__(self):
        return self.ticket.event.title + ' - ' + self.customer.name

