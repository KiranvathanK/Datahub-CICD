from datahub_v3_app.models import role_api
from rest_framework import serializers


class role_api_serializer(serializers.ModelSerializer):

    class Meta:
        model= role_api
        fields= ['id','role_name','role_desc','role_start_date','role_end_date','role_status']