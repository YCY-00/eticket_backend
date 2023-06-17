from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import TicketModel
from .serializers import TicketModelSerializer

class TicketTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.ticket_data = {
            "event": "some event",
            "price": 100.0,
        }
        self.ticket = TicketModel.objects.create(**self.ticket_data)

    def test_get_ticket(self):
        response = self.client.get(reverse('get_ticket', kwargs={'id': self.ticket.id}))
        ticket = TicketModel.objects.get(id=self.ticket.id)
        serializer = TicketModelSerializer(ticket)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_get_tickets(self):
        response = self.client.get(reverse('get_tickets'))
        tickets = TicketModel.objects.all()
        serializer = TicketModelSerializer(tickets, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_register_ticket(self):
        response = self.client.post(
            reverse('register_ticket'),
            self.ticket_data,
            format="json"
        )
        self.assertEqual(response.status_code, 200)

    def test_update_ticket(self):
        update_ticket_data = {
            "event": "updated event",
            "price": 200.0,
        }
        response = self.client.put(
            reverse('update_ticket', kwargs={'id': self.ticket.id}),
            update_ticket_data,
            format="json"
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_ticket(self):
        response = self.client.delete(reverse('delete_ticket', kwargs={'id': self.ticket.id}))
        self.assertEqual(response.status_code, 200)


# Create your tests here.
