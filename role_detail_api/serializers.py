from rest_framework import serializers
from datahub_v3_app.models import role_details_api


class role_detail_serializer(serializers.ModelSerializer):

    class Meta:
        model= role_details_api
        fields= ['id','role_name','role_detail_name','role_description','role_handling_pages','read','write']