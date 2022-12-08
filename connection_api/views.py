from django.shortcuts import render
from ast import Delete
from django.http.response import Http404
from urllib import response
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from datahub_v3_app.models import connection
from rest_framework.views import APIView
from rest_framework import status
from connection_api.serializers import ConnectionsSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions ,filters



class ListConnectionsAPIView(ListAPIView):
    queryset = connection.objects.all()
    serializer_class = ConnectionsSerializer
    # permission_classes = (IsAuthenticated)

    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]

    filterset_fields = ['id','connection_name']
    search_fields = ['connection_name']
    ordering_fields = ['id', 'connection_name']
    def get_user_by_pk(self, pk):
        try:
            return connection.objects.get(pk=pk)
        except:
            return Response({
                'error': 'does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None):

        if pk:
                reg = self.get_user_by_pk(pk)
                serializer = ConnectionsSerializer(reg)
                return Response([serializer.data])

        else:
                reg = connection.objects.all()
                serializer = ConnectionsSerializer(reg, many=True)
                return Response(serializer.data)

class CreateConnectionsAPIView(CreateAPIView):
    queryset = connection.objects.all()
    serializer_class = ConnectionsSerializer

   
class UpdateConnectionsAPIView(UpdateAPIView):
    queryset = connection.objects.all()
    serializer_class = ConnectionsSerializer

    def put(self, request, pk=None, format=None):
        conn_to_update = connection.objects.get(pk=pk)
        serializer = ConnectionsSerializer(instance=conn_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'connections Updated Successfully',
            'data': serializer.data
        }

        return response

class DeleteConnectionsAPIView(DestroyAPIView):
    queryset = connection.objects.all()
    serializer_class = ConnectionsSerializer

    def delete(self, request, pk, format=None):
        todo_to_delete =  connection.objects.get(pk=pk)

        todo_to_delete.delete()

        return Response({
            'message': 'connections Deleted Successfully'
        })