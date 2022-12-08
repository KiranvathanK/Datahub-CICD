from ast import Delete
from django.http.response import Http404
from urllib import response
from django.shortcuts import render
from rest_framework import generics
from datahub_v3_app.models import pipeline
from rest_framework.views import APIView
from pipeline_api.serializers import pipline_Serializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



class pipe(APIView):
    def get_object(self, pk):
            try:
                return pipeline.objects.get(pk=pk)
            except pipeline.DoesNotExist:
                raise Http404
    def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = pipline_Serializer(data)
                return Response([serializer.data])

            else:
                data = pipeline.objects.all()
                serializer = pipline_Serializer(data, many=True)

                return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data

        serializer = pipline_Serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Created Successfully',
            'data': serializer.data
            }

        return response

    def put(self, request, pk=None, format=None):
        conn_to_update = pipeline.objects.get(pk=pk)
        serializer = pipline_Serializer(instance=conn_to_update,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Updated Successfully',
            'data': serializer.data
        }
        return response

    def delete(self, request, pk, format=None):
        conect_to_delete = pipeline.objects.get(pk=pk)
        conect_to_delete.delete()
        return Response({
            'message': 'Deleted Successfully'
        })