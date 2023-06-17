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

# 특정 티켓을 얻는 API
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_ticket(request, id):
    try:
        ticket = TicketModel.objects.get(id=id)  # 특정 id에 해당하는 티켓을 가져옵니다
        serializer = TicketModelSerializer(ticket)
        return Response({"status": "success", "data": serializer.data})  # 티켓 정보를 리턴합니다
    except TicketModel.DoesNotExist:  # 만약 티켓이 존재하지 않을 경우
        return Response(
            {"status": "failed", "message": "Ticket not found"},
            status=400,
        )

# 모든 티켓을 얻는 API
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_tickets(request):
    try:
        tickets = TicketModel.objects.all()  # 모든 티켓을 가져옵니다
        serializer = TicketModelSerializer(tickets, many=True)
        return Response({"status": "success", "data": serializer.data})  # 모든 티켓 정보를 리턴합니다
    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)},  # 오류가 발생한 경우
            status=400,
        )

# 새 티켓을 등록하는 API
@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def register_ticket(request):
    try:
        serializer = TicketModelSerializer(data=request.data)  # 요청 데이터로부터 Serializer를 생성합니다
        if serializer.is_valid():
            serializer.save()  # Serializer가 유효하다면 데이터를 저장합니다
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response(
                {"status": "failed", "message": serializer.errors},  # Serializer가 유효하지 않은 경우 오류 메시지를 리턴합니다
                status=400,
            )
    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)},  # 오류가 발생한 경우
            status=400,
        )

# 티켓 정보를 업데이트하는 API
@api_view(["PUT"])
@permission_classes((permissions.AllowAny,))
def update_ticket(request, id):
    try:
        ticket = TicketModel.objects.get(id=id)  # 특정 id에 해당하는 티켓을 가져옵니다
        serializer = TicketModelSerializer(ticket, data=request.data)  # 요청 데이터로부터 Serializer를 생성합니다
        if serializer.is_valid():
            serializer.save()  # Serializer가 유효하다면 데이터를 저장합니다
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response(
                {"status": "failed", "message": serializer.errors},  # Serializer가 유효하지 않은 경우 오류 메시지를 리턴합니다
                status=400,
            )
    except TicketModel.DoesNotExist:  # 만약 티켓이 존재하지 않을 경우
        return Response(
            {"status": "failed", "message": "Ticket not found"},
            status=400,
        )

# 티켓을 삭제하는 API
@api_view(["DELETE"])
@permission_classes((permissions.AllowAny,))
def delete_ticket(request, id):
    try:
        ticket = TicketModel.objects.get(id=id)  # 특정 id에 해당하는 티켓을 가져옵니다
        ticket.delete()  # 티켓을 삭제합니다
        return Response({"status": "success"})
    except TicketModel.DoesNotExist:  # 만약 티켓이 존재하지 않을 경
        return Response(
            {"status": "failed", "message": "Ticket not found"},
            status=400,
        )
