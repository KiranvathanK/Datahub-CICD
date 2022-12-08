from dataclasses import fields
from rest_framework import serializers
from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import Http404
from urllib import response
from rest_framework.response import Response
import requests

class user_profile(APIView):
    def hpots(request):
        profile_list=requests.get('http://34.73.32.172:8000/profile').json()
        new_profile=[]
        for profiles in profile_list:
            temp_profile={}
            temp_profile['id']=profiles['id']
            temp_profile['first_name']=profiles['first_name']
            temp_profile['last_name']=profiles['last_name']
            temp_profile['email']=profiles['email']
            new_profile.append(temp_profile)
        return (new_profile)
    def get(self,request):
        data=self.hpots()
        return Response(data)