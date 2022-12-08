from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from urllib import response
from django.http.response import Http404
from  datahub_v3_app.models import pages
from.serializers import *

# Create your views here.
class page_cl(APIView):
    def get_object(self, pk):
            try:
                return pages.objects.get(pk=pk)
            except pages.DoesNotExist:
                raise Http404
    def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = pagedetserializer(data)
                return Response(serializer.data)

            else:
                data = pages.objects.all()
                serializer = pagedetserializer(data, many=True)

                return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = pagedetserializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': ' Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        conn_to_update = pages.objects.get(pk=pk)
        serializer = pagedetserializer(instance=conn_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': ' Updated Successfully',
            'data': serializer.data
        }

        return response
    
        
    def delete(self, request, pk, format=None):
        conect_to_delete =  pages.objects.get(pk=pk)

        conect_to_delete.delete()

        return Response({
            'message': ' Deleted Successfully'
        })