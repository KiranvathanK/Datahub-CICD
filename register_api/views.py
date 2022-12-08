import email
from urllib import response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from register_api.serializers import UserSerializer
from datahub_v3_app.models import User
from rest_framework import status
import logging

logger = logging.getLogger("mylogger")




class RegisterView(APIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
     
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {
                "message": "Register Successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)  
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST) 
      