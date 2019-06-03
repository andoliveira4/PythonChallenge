from rest_framework import generics
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status
from .util import executeChallenge


class CalculaHistograma(generics.CreateAPIView):
    """
    POST validation/
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        
        _id = int(request.data.get("id", ""))
        _img = request.data.get("img", "")
        _x1 = int(request.data.get("x1", ""))
        _y1 = int(request.data.get("y1", ""))
        _x2 = int(request.data.get("x2", ""))
        _y2 = int(request.data.get("y2", ""))

        _result = executeChallenge(_img,_x1,_y1,_x2,_y2)

        return Response(
                data={
                    "id": _id,
                    "img": _img,
                    "x1": _x1,
                    "y1": _y1,
                    "x2": _x2,
                    "y2": _y2,
                    "result": _result,
                },
                status=status.HTTP_200_OK
            )
