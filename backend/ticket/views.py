from rest_framework import views, permissions
from rest_framework.response import Response
from .models import TicketModel
from .serializers import TicketSerializer
from drf_spectacular.utils import extend_schema
from rest_framework import status


class GetTicketView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TicketSerializer

    def get(self, request, ticket_id: str):
        try:
            ticket = TicketModel.objects.get(id=ticket_id)
            return Response(data=TicketSerializer(ticket).data, status=200)
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


@extend_schema(responses={status.HTTP_200_OK: TicketSerializer(many=True)})
class GetTicketsView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TicketSerializer

    def get(self, request):
        try:
            tickets = TicketModel.objects.all()
            return Response(data=TicketSerializer(tickets, many=True).data, status=200)
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


class RegisterTicketView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TicketSerializer

    def post(self, request):
        try:
            ticket = TicketModel.objects.create(**request.data)
            return Response(data=TicketSerializer(ticket).data, status=200)
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


class UpdateTicketView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TicketSerializer

    def put(self, request, ticket_id: str):
        try:
            ticket = TicketModel.objects.get(id=ticket_id)
            serializer = TicketSerializer(ticket, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=200)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


class DeleteTicketView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TicketSerializer

    def delete(self, request, ticket_id: str):
        try:
            ticket = TicketModel.objects.get(id=ticket_id)
            ticket.delete()
            return Response(data={"status": "success"}, status=200)

        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)
