from rest_framework import serializers
from datahub_v3_app.models import pipeline_details


class Pipeline_detailserializer(serializers.ModelSerializer):

    class Meta:
        model= pipeline_details
        fields = '__all__'
        # fields= ['Pipeline_details_id','Pipeline_detail_name','pipeline_dtls_desc','Pipeline_id','db_SQL_id','SQL_extract_name',
        # 'Target_table_name','Source_table_name','start_date','end_date','Pipeline_dtls_status','last_modified_by','last_modified_on','created_on',
        # 'created_by','is_active','Pipeline_dtls_bench_mark_commit','pipeline_dtls_parallel_load_allowed','Pipeline_dtls_parallel_thread_count',
        # 'Pipeline_dtls_truncate_load']