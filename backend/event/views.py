from rest_framework import views, permissions
from rest_framework.response import Response
from backend.event.serializers import EventSerializer
from backend.payment.models import PaymentModel
from backend.ticket.models import TicketModel
from backend.users.api.serializers import UserSerializer
from .models import EventModel
import datetime
from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import status


class GetEventView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = EventSerializer

    def get(self, request, event_id: str):
        try:
            event = EventModel.objects.get(id=event_id)
            return Response(data=EventSerializer(event).data, status=200)
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


@extend_schema(responses={status.HTTP_200_OK: EventSerializer(many=True)})
class GetEventsView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = EventSerializer

    def get(self, request):
        try:
            events = EventModel.objects.all()
            return Response(data=EventSerializer(events, many=True).data, status=200)
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


@extend_schema(responses={status.HTTP_200_OK: UserSerializer(many=True)})
class GetParticipantsView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def get(self, request, event_id: str):
        try:
            event = EventModel.objects.get(id=event_id)

            ticket = TicketModel.objects.get(event=event)
            payments = PaymentModel.objects.filter(ticket=ticket)

            customers = [payment.customer for payment in payments]

            return Response(data=UserSerializer(customers, many=True).data, status=200)

        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


class RegisterEventView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = EventSerializer

    def post(self, request):
        try:
            if not request.user.is_organizer and not request.user.is_admin:
                return Response({"status": "failed", "message": "You are not authorized to do this"}, status=400)

            date = request.data["date"]
            title = request.data["title"]
            location = request.data["location"]
            capacity = request.data["capacity"]

            event = EventModel.objects.create(
                date=datetime.datetime.fromtimestamp(date),
                title=title,
                location=location,
                capacity=capacity,
                remaining_capacity=capacity,
                organizer=request.user,
            )

            return Response({"status": "success"})
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


class UpdateEventView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = EventSerializer

    def put(self, request, event_id: str):
        try:
            event = EventModel.objects.get(id=event_id)

            title = request.data.get("title", None)
            if title:
                event.title = title

            date = request.data["date"]
            if date:
                event.date = datetime.datetime.fromtimestamp(date)

            location = request.data.get("location", None)
            if location:
                event.location = location

            ticket = TicketModel.objects.filter(event=event)
            payments = PaymentModel.objects.filter(ticket=ticket)

            capacity = request.data.get("capacity", None)
            if capacity:
                if capacity < len(payments):
                    return Response(
                        {"status": "failed", "message": "Capacity is less than the number of participants"}, status=400
                    )

                event.capacity = capacity
                event.remaining_capacity = capacity

            return Response({"status": "success"})
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


class DeleteEventView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = EventSerializer

    def delete(self, request, event_id: str):
        try:
            event = EventModel.objects.get(id=event_id)
            event.delete()

            return Response({"status": "success"})
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)
