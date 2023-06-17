from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.response import Response

from rest_framework import permissions


# Create your views here.
@api_view(["GET"])
@permission_classes((permissions.IsAuthenticated,))
def get_event(request):
    try:
        # do something
        return Response({"status": "success"})
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
        # do something
        return Response({"status": "success"})
    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)},
            status=400,
        )


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_participants(request):
    try:
        # do something
        return Response({"status": "success"})
    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)},
            status=400,
        )


# Create your views here.
@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def register_event(request):
    try:
        # do something
        return Response({"status": "success"})
    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)},
            status=400,
        )


@api_view(["PUT"])
@permission_classes((permissions.AllowAny,))
def update_event(request):
    try:
        # do something
        return Response({"status": "success"})
    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)},
            status=400,
        )


@api_view(["DELETE"])
@permission_classes((permissions.AllowAny,))
def delete_event(request):
    try:
        # do something
        return Response({"status": "success"})
    except Exception as e:
        return Response(
            {"status": "failed", "message": str(e)},
            status=400,
        )
