from datahub_v3_app.models import db_sql_table
from rest_framework.views import APIView
from db_sql_extract.serializers import dbextract_Serializer
from rest_framework.response import Response
from django.http.response import Http404
from rest_framework import status
from rest_framework.generics import CreateAPIView


# Create your views here.

class db_sql_extract(APIView):
    def get_user_by_pk(self, pk):
        try:
            return db_sql_table.objects.get(pk=pk)
        except:
            return Response({
                'error': 'does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None):

        if pk:
                reg = self.get_user_by_pk(pk)
                serializer = dbextract_Serializer(reg)
                return Response([serializer.data])

        else:
                reg = db_sql_table.objects.all()
                serializer = dbextract_Serializer(reg, many=True)
                return Response(serializer.data)


    def post(self, request, format=None):
        data = request.data
        serializer = dbextract_Serializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': ' Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        conn_to_update = db_sql_table.objects.get(pk=pk)
        serializer = dbextract_Serializer(instance=conn_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': ' Updated Successfully',
            'data': serializer.data
        }

        return response
    def delete(self, request, pk, format=None):
        todo_to_delete =  db_sql_table.objects.get(pk=pk)

        todo_to_delete.delete()

        return Response({
            'message': ' Deleted Successfully'
        })