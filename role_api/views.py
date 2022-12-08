from django.shortcuts import render
from role_api.serializers import role_api_serializer
from ast import Delete
from urllib import response
from django.shortcuts import render
from datahub_v3_app.models import role_api
from rest_framework import generics
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class role_name_api(APIView):
    def get_object(self, pk):
            try:
                return role_api.objects.get(pk=pk)
            except role_api.DoesNotExist:
                raise Http404



    def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = role_api_serializer(data)
                return Response(serializer.data)


            else:
                data = role_api.objects.all()
                serializer = role_api_serializer(data, many=True)

                return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = role_api_serializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Role Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        conn_to_update = role_api.objects.get(pk=pk)
        serializer = role_api_serializer(instance=conn_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Role Updated Successfully',
            'data': serializer.data
        }

        return response
    def delete(self, request, pk, format=None):
        conect_to_delete =  role_api.objects.get(pk=pk)

        conect_to_delete.delete()

        return Response({
            'message': 'Role Deleted Successfully'
        })