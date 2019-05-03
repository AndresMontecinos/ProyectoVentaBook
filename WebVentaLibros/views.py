from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import libro
from .serializers import libroSerializers


# Create your views here.

class libroList(APIView):

    def get(self, request):
        libro1 = libro.objects.all()
        serializers = libroSerializers(libro1, many=True)
        return Response(serializers.data)

    def post(self):
        pass