from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from urllib import request
from rest_framework.response import Response
from datahub_v3_app.models import *
from role_detail_api.serializers import *

# Create your views here.
class role_details(APIView):
    def get_object(self, pk):
            try:
                return role_details_api.objects.get(pk=pk)
            except role_details_api.DoesNotExist:
                raise Http404
    def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = role_detail_serializer(data)
                return Response(serializer.data)

            else:
                data = role_details_api.objects.all()
                serializer = role_detail_serializer(data, many=True)

                return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = role_detail_serializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': ' Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        conn_to_update = role_details_api.objects.get(pk=pk)
        serializer = role_detail_serializer(instance=conn_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': ' Updated Successfully',
            'data': serializer.data
        }

        return response
    def delete(self, request, pk, format=None):
        conect_to_delete =  role_details_api.objects.get(pk=pk)

        conect_to_delete.delete()
        return Response({
            'message': ' Deleted Successfully'
        })