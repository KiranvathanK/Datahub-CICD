from ast import Delete
from django.http.response import Http404
from urllib import response
from django.shortcuts import render
from rest_framework import generics
from datahub_v3_app.models import db_config
from rest_framework.views import APIView
from db_config_api.serializers import db_configserializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class db_config_api(APIView):
    def get_object(self, pk):
            try:
                return db_config.objects.get(pk=pk)
            except db_config.DoesNotExist:
                raise Http404
    def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = db_configserializer(data)
                return Response(serializer.data)

            else:
                data = db_config.objects.all()
                serializer = db_configserializer(data, many=True)

                return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = db_configserializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'connect_detail Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        conn_to_update = db_confog.objects.get(pk=pk)
        serializer = db_configserializer(instance=conn_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'conect_detail Updated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self, request, pk, format=None):
        todo_to_delete =db_config.objects.get(pk=pk)

        todo_to_delete.delete()

        return Response({
            'message': 'connect_detail Deleted Successfully'
        })