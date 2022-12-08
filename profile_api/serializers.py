from dataclasses import dataclass
import email
import imp
from urllib import request
from rest_framework import serializers
from datahub_v3_app.models import User
from django.forms import ValidationError
import logging
import json


class UserSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(required=True)
    last_name = serializers.CharField(required=False)
    email=serializers.CharField(required=True),
    phone_number=serializers.CharField(required=True),
    password=serializers.CharField(required=True),
    alternate_phonenumber=serializers.CharField(required=False),
    addressline_one=serializers.CharField(required=True),
    addressline_two=serializers.CharField(required=False),
    countryor_city=serializers.CharField(required=True),
    postalcode=serializers.CharField(required=True)
    company_name=serializers.CharField(required=False),
    company_type=serializers.CharField(required=False),
    category=serializers.CharField(required=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}    
        }
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance