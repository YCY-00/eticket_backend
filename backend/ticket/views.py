from django.shortcuts import render
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework import permissions
from .models import TicketModel
from .serializers import TicketModelSerializer

from .models import TicketModel
from .serializers import TicketModelSerializer

@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_ticket(request, id):
    try:
        ticket = TicketModel.objects.get(id=id)
        serializer = TicketModelSerializer(ticket)
        return Response({"status": "success", "data": serializer.data}) 
    except TicketModel.DoesNotExist: 
        return Response(
            {"status": "failed", "message": "Ticket not found"},
            status=400,
        )

@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_tickets(request):
    try:
        tickets = TicketModel.objects.all() 
        serializer = TicketModelSerializer(tickets, many=True)
        return Response({"status": "success", "data": serializer.data}) 
    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)}, 
            status=400,
        )

@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def register_ticket(request):
    try:
        serializer = TicketModelSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save() 
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response(
                {"status": "failed", "message": serializer.errors},
                status=400,
            )
    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)}, 
            status=400,
        )

@api_view(["PUT"])
@permission_classes((permissions.AllowAny,))
def update_ticket(request, id):
    try:
        ticket = TicketModel.objects.get(id=id) 
        serializer = TicketModelSerializer(ticket, data=request.data) 
        if serializer.is_valid():
            serializer.save()  # Serializer가 유효하다면 데이터를 저장합니다
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response(
                {"status": "failed", "message": serializer.errors},
                status=400,
            )
    except TicketModel.DoesNotExist: 
        return Response(
            {"status": "failed", "message": "Ticket not found"},
            status=400,
        )

@api_view(["DELETE"])
@permission_classes((permissions.AllowAny,))
def delete_ticket(request, id):
    try:
        ticket = TicketModel.objects.get(id=id)
        ticket.delete() 
        return Response({"status": "success"})
    except TicketModel.DoesNotExist: 
        return Response(
            {"status": "failed", "message": "Ticket not found"},
            status=400,
        )
