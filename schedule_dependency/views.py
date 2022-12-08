from django.shortcuts import render

from schedule_dependency.serializers import S_Dependency_Serializer
from rest_framework.views import APIView  
from rest_framework.response import Response     
from rest_framework import status
from rest_framework.generics import CreateAPIView
from datahub_v3_app.models import ScheduleDependency 
from django.http.response import Http404




class schedule_dep(APIView):
    def get_user_by_pk(self, pk):
        try:
            return ScheduleDependency.objects.get(pk=pk)
        except:
            return Response({
                'error': 'does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None):

        if pk:
                reg = self.get_user_by_pk(pk)
                serializer = S_Dependency_Serializer(reg)
                return Response([serializer.data])

        else:
                reg = ScheduleDependency.objects.all()
                serializer = S_Dependency_Serializer(reg, many=True)
                return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = S_Dependency_Serializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': ' Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        conn_to_update = ScheduleDependency.objects.get(pk=pk)
        serializer = S_Dependency_Serializer(instance=conn_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Updated Successfully',
            'data': serializer.data
        }

        return response
    def delete(self, request, pk, format=None):
        todo_to_delete =  ScheduleDependency.objects.get(pk=pk)

        todo_to_delete.delete()

        return Response({
            'message': 'Deleted Successfully'
        })






# # Create your views here.
# class get_schedule(APIView):
#     def get_user_by_pk(self,pk):
#         # import pdb
#         # pdb.set_trace()
#         try:
#             return ScheduleDependency.objects.get(pk=pk)
#         except:
#             return Response ({
#                 'error': 'does not exist'
#             },status=status.HTTP_404_NOT_FOUND)
    
#     def get(self,request,pk=None):
#         # import pdb
#         # pdb.set_trace()
#         if pk:
#             reg = self.get_user_by_pk(pk)
#             serializer = S_Dependency_Serializer(reg)
#             return Response([serializer.data])
        
#         else:
#             reg = ScheduleDependency.objects.all()
#             serializer = S_Dependency_Serializer(reg, many=True)
#             return Response(serializer.data)

    

# class post_schedule(APIView):
#     serializer_class = S_Dependency_Serializer
#     def post(self, request):
#         serializer = S_Dependency_Serializer(data=request.data)
     
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             response = {
#                 "message": "Successfully Created"
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)  
#         return Response(data=response, status=status.HTTP_400_BAD_REQUEST)  


# class update_schedule(APIView):
#     def get_user_by_pk(self,pk):
#         try:
#             return ScheduleDependency.objects.get(pk=pk)
#         except:
#             return Response ({
#                 'error': 'does not exist'
#             },status=status.HTTP_404_NOT_FOUND)
    
#     def get(self,request,pk):
#         reg = self.get_user_by_pk(pk)
#         serializer = S_Dependency_Serializer(reg)
#         return Response(serializer.data)


#     # def put(self,request,pk):
#     #     reg = self.get_user_by_pk(pk)
#     #     if request.method == 'PUT':
#     #         serializer = S_Dependency_Serializer(reg,data=request.data)
#     #         if serializer.is_valid():
#     #             serializer.save()
#     #             response = Response()
#     #             response.data = {
#     #                 'message': 'Updated Successfully',
#     #                 'data': serializer.data
#     #             }
#     #             return response

#     #         else:
#     #             return serializer.errors


#     def put(self, request, pk=None, format=None):
#         conn_to_update = ScheduleDependency.objects.get(pk=pk)
#         serializer = ScheduleDependency

#         serializer.is_valid(raise_exception=True)

#         serializer.save()

#         response = Response()

#         response.data = {
#             'message': 'Updated Successfully',
#             'data': serializer.data
#         }

#         return response

#     def delete(self,request,pk):
#             reg = self.get_user_by_pk(pk)
#             reg.delete()
#             return Response({
#                 'message': 'Deleted successfully'},
#                 status=status.HTTP_204_NO_CONTENT)
