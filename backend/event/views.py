import datetime
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework.request import Request
from backend.event.serializers import EventSerializer
from backend.payment.models import PaymentModel
from backend.ticket.models import TicketModel
from backend.users.api.serializers import UserSerializer
from .models import EventModel
from rest_framework import permissions


# Create your views here.
@api_view(["GET"])
@permission_classes((permissions.IsAuthenticated,))
def get_event(request, event_id: str):
    try:
        event = EventModel.objects.get(id=event_id)
        return Response(data=EventSerializer(event).data, status=200)
    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)},
            status=400,
        )


# Create your views here.
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_events(request):
    try:
        events = EventModel.objects.all()
        return Response(data=EventSerializer(events, many=True).data, status=200)
    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)},
            status=400,
        )


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_participants(request, event_id: str):
    try:
        event = EventModel.objects.get(id=event_id)

        ticket = TicketModel.objects.filter(event=event)
        payments = PaymentModel.objects.filter(ticket=ticket)

        customers = []
        for payment in payments:
            customers.append(payment.customer)

        return Response(data=UserSerializer(data=customers, many=True).data, status=200)

    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)},
            status=400,
        )


# Create your views here.
@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def register_event(request: Request):
    try:
        if not request.user.is_organizer and not request.user.is_admin:
            return Response(
                {"status": "failed", "message": "You are not authorized to do this"},
                status=400,
            )

        date: int = request.data["date"]
        title: str = request.data["title"]
        location: str = request.data["location"]
        capacity: int = request.data["capacity"]

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
        return Response(
            {"status": "failed", "message": str(e)},
            status=400,
        )


@api_view(["PUT"])
@permission_classes((permissions.AllowAny,))
def update_event(request: Request, event_id: str):
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
                    {"status": "failed", "message": "Capacity is less than the number of participants"},
                    status=400,
                )

            event.capacity = capacity
            event.remaining_capacity = capacity

        return Response({"status": "success"})
    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)},
            status=400,
        )


@api_view(["DELETE"])
@permission_classes((permissions.AllowAny,))
def delete_event(request, event_id: str):
    try:
        event = EventModel.objects.get(id=event_id)
        event.delete()

        return Response({"status": "success"})
    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)},
            status=400,
        )
