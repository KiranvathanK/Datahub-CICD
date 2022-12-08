from dataclasses import fields
from rest_framework import serializers
from datahub_v3_app.models import connection_detail

class connection_details_keypairsserializer(serializers.ModelSerializer):

    class Meta:
        model= connection_detail
        fields = '__all__'
        # fields= ['id','connection_name','connection_detail','conn_pd_id','key_pram','value_pram','start_date','end_date','last_modified_by',
        # 'last_modified_on','created_on','created_by','is_active']