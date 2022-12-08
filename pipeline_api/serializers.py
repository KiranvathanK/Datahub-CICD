from rest_framework import serializers
from datahub_v3_app.models import pipeline
class pipline_Serializer(serializers.ModelSerializer):

    #description = serializers.SerializerMethodField()

    class Meta:
        model =  pipeline
        fields = ['id','pipeline_name','configuration_name','email','Description','Start_date','End_date','is_active','config_id']