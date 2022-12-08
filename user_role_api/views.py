from dataclasses import fields
from rest_framework import serializers
from datahub_v3_app.models import user_role_view
from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import Http404
from urllib import response
from rest_framework.response import Response
import requests
from user_role_api.serializers import users_role_viewserializer

class user_role(APIView):
    def get_object(self, pk):
            try:
                return user_role_view.objects.get(pk=pk)
            except user_role_view.DoesNotExist:
                raise Http404
    def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = users_role_viewserializer(data)
                return Response(serializer.data)

            else:
                data = user_role_view.objects.all()
                serializer = users_role_viewserializer(data, many=True)

                return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = users_role_viewserializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': ' Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        conn_to_update = user_role_view.objects.get(pk=pk)
        serializer = users_role_viewserializer(instance=conn_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': ' Updated Successfully',
            'data': serializer.data
        }

        return response
    def delete(self, request, pk, format=None):
        conect_to_delete =  user_role_view.objects.get(pk=pk)

        conect_to_delete.delete()

        return Response({
            'message': ' Deleted Successfully'
        })