# Create your views here.
from ast import Delete
from django.http.response import Http404
from urllib import response
from django.shortcuts import render
from rest_framework import generics
from datahub_v3_app.models import connection_detail
from rest_framework.views import APIView
from connection_details_api.serializers import connection_details_keypairsserializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class detail(APIView):
    def get_object(self, pk):
            try:
                return connection_detail.objects.get(pk=pk)
            except connection_detail.DoesNotExist:
                raise Http404
    def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = connection_details_keypairsserializer(data)
                return Response([serializer.data])

            else:
                data = connection_detail.objects.all()
                serializer = connection_details_keypairsserializer(data, many=True)

                return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = connection_details_keypairsserializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'connect_detail Created Successfully',
            'data': serializer.data
        }
        return response

    def put(self, request, pk=None, format=None):
        conn_to_update = connection_detail.objects.get(pk=pk)
        serializer = connection_details_keypairsserializer(instance=conn_to_update,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'conect_detail Updated Successfully',
            'data': serializer.data
        }
        return response

    def delete(self, request, pk, format=None):
        conect_to_delete =  connection_detail.objects.get(pk=pk)
        conect_to_delete.delete()
        return Response({
            'message': 'connect_detail Deleted Successfully'
        })