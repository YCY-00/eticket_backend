from rest_framework import views, permissions
from rest_framework.response import Response
from .models import NotificationModel
from .serializers import NotificationSerializer
from drf_spectacular.utils import extend_schema
from rest_framework import status


class GetNotificationView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = NotificationSerializer

    def get(self, request, notification_id: str):
        try:
            notification = NotificationModel.objects.get(id=notification_id)
            return Response(data=NotificationSerializer(notification).data, status=200)
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


@extend_schema(responses={status.HTTP_200_OK: NotificationSerializer(many=True)})
class GetNotificationsView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = NotificationSerializer

    def get(self, request):
        try:
            notifications = NotificationModel.objects.all()
            return Response(data=NotificationSerializer(notifications, many=True).data, status=200)
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


class RegisterNotificationView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = NotificationSerializer

    def post(self, request):
        try:
            notification = NotificationModel.objects.create(**request.data)
            return Response(data=NotificationSerializer(notification).data, status=200)
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


class UpdateNotificationView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = NotificationSerializer

    def put(self, request, notification_id: str):
        try:
            notification = NotificationModel.objects.get(id=notification_id)
            serializer = NotificationSerializer(notification, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=200)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)


class DeleteNotificationView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = NotificationSerializer

    def delete(self, request, notification_id: str):
        try:
            notification = NotificationModel.objects.get(id=notification_id)
            notification.delete()
            return Response(data={"status": "success"}, status=200)

        except Exception as e:
            return Response({"status": "failed", "message": str(e)}, status=400)
