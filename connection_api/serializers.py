from rest_framework import serializers
from datahub_v3_app.models import connection

class ConnectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = connection
        fields = "__all__"