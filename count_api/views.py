from datahub_v3_app.models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from count_api.serializers import count_serializer
from django.http.response import Http404



class count_api(APIView):


    def get(self, request, pk=None, format=None):
          if pk:
                data = self.get_object(pk)
                serializer = count_serializer(data)

          else:
                data =role_api.objects.all()
                serializer = count_serializer(data, many=True)

                message_count2 = pipiline_sch.objects.filter(pipeline_status='True').count()
                message_count6 = pipline_table.objects.filter(is_active='True').count()
                message_count7 = con_detail.objects.filter(is_active='True').count()
                message_count8 = db_conf.objects.filter(is_active='True').count()
                message_count9 = pipiline_sch.objects.filter(pipeline_status='False').count()
                message_count10 = pipline_table.objects.filter(is_active='False').count()
                message_count11 = con_detail.objects.filter(is_active='False').count()
                message_count12 = db_conf.objects.filter(is_active='False').count()




                response = Response()

                response.data = {


                    'active pipeline schedule':message_count2,
                    'active pipeline': message_count6,
                    'active connection': message_count7,
                    'active configurations': message_count8,

                    'inactive pipeline schedule':message_count9,
                    'inactive pipeline':message_count10,
                    'inactive connection':message_count11,
                    'inactive configurations':message_count12,

                    'total pipeline schedule':message_count2+message_count9,
                    'total pipeline':message_count6+message_count10,
                    'total connection':message_count7+message_count11,
                    'total configurations':message_count8+message_count12



                }
                return response