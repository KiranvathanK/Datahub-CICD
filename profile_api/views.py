from django.shortcuts import render
from rest_framework.views import APIView
#from.models import pipe_line
#from .serializers import pipe_lineserializer
from django.http.response import Http404
from urllib import response
from rest_framework.response import Response
import requests
from datahub_v3_app.models import User
from profile_api.serializers import UserSerializer

class profile(APIView):
    def get_object(self, pk):
            try:
                return User.objects.get(pk=pk)
            except User.DoesNotExist:
                raise Http404
    def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = UserSerializer(data)
                return Response(serializer.data)

            else:
               data = User.objects.all()
               serializer = UserSerializer(data, many=True)

               return Response(serializer.data)