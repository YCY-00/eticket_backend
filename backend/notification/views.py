from django.shortcuts import render
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.response import Response

from rest_framework import permissions

from .models import NotificationModel
from .serializers import NotificaitonModelSerializer

# Create your views here.
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_notification(request, id):
    try:
        Notification = NotificationModel.objects.get(id = id)
        serializer = NotificationModelSerializer(Notification)
        return Response({"status": "success", "data": serializer.data}) 
    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)},
            status=400,
        )


# Create your views here.
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_notifications(request):
    try:
        # do something
        Notifications = TicketModel.objects.all() 
        serializer =  NotificationModelSerializer(Notifications, many=True)
        return Response({"status": "success", "data": serializer.data})
    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)},
            status=400,
        )


# Create your views here.
@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def register_notification(request):
    try:
        serializer =  NotificationModelSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save() 
            return Response({"status": "success", "data": serializer.data})
        return Response({"status": "success"})
    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)},
            status=400,
        )


@api_view(["PUT"])
@permission_classes((permissions.AllowAny,))
def update_notification(request, id):
    try:
        # do something
        notification = NotificationModel.objects.get(id = id) # what data should we get?
        serializer = NotificationModelSerializer(ticket, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response(
                {"status": "failed", "message": serializer.errors},
                status=400,
            )
        return Response({"status": "success"})
    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)},
            status=400,
        )


@api_view(["DELETE"])
@permission_classes((permissions.AllowAny,))
def delete_notification(request, id):
    try:
        # do something
        notification = NotificationModel.objects.get(id=id)
        notification.delete() 
        return Response({"status": "success"})
    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)},
            status=400,
        )

