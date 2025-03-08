from rest_framework import views, permissions
from rest_framework.response import Response
from backend.event.models import EventModel
from backend.users.models import User
from backend.ticket.serializers import TicketSerializer
from .serializers import PaymentSerializer
from .models import PaymentModel

from drf_spectacular.utils import extend_schema
from rest_framework import status


class GetPaymentTicketView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TicketSerializer

    def get(self, request, payment_id: str):
        try:
            payment = PaymentModel.objects.get(id=payment_id)
            ticket = payment.ticket
            return Response(data=TicketSerializer(ticket).data, status=200)
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


class GetPaymentView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PaymentSerializer

    def get(self, request, payment_id: str):
        try:
            payment = PaymentModel.objects.get(id=payment_id)
            return Response(data=PaymentSerializer(payment).data, status=200)
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


class RegisterPaymentView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PaymentSerializer

    def post(self, request):
        try:
            payment = PaymentModel.objects.create(**request.data)
            return Response(data=PaymentSerializer(payment).data, status=200)
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


class UpdatePaymentView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PaymentSerializer

    def put(self, request, payment_id: str):
        try:
            payment = PaymentModel.objects.get(id=payment_id)
            serializer = PaymentSerializer(payment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=200)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


class DeletePaymentView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PaymentSerializer

    def delete(self, request, payment_id: str):
        try:
            payment = PaymentModel.objects.get(id=payment_id)
            payment.delete()
            return Response(data={"status": "success"}, status=200)
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


@extend_schema(responses={status.HTTP_200_OK: PaymentSerializer(many=True)})
class GetEventPaymentsView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PaymentSerializer

    def get(self, request, event_id: str):
        try:
            event = EventModel.objects.get(id=event_id)
            payments = PaymentModel.objects.filter(event=event)
            return Response(data=PaymentSerializer(payments, many=True).data, status=200)
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


@extend_schema(responses={status.HTTP_200_OK: PaymentSerializer(many=True)})
class GetUserPaymentsView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PaymentSerializer

    def get(self, request, user_id: str):
        try:
            print("here")
            user = User.objects.get(id=user_id)
            payments = PaymentModel.objects.filter(customer=user)
            return Response(data=PaymentSerializer(payments, many=True).data, status=200)
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)
