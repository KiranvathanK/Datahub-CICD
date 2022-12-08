"""datahub_v3_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from login_api.views import LoginView
from register_api.views import RegisterView
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from connection_api.views import ListConnectionsAPIView,CreateConnectionsAPIView,UpdateConnectionsAPIView,DeleteConnectionsAPIView 
from schedule_dependency.views import schedule_dep
from db_sql_extract.views import db_sql_extract
from pipeline_schedule_api.views import pipeline_sch
from pipeline_api.views import pipe
from pipeline_details_api.views import Pipeline_detail
from connection_details_api.views import detail
from db_config_api.views import db_config_api
from role_api.views import role_name_api
from role_detail_api.views import role_details
from profile_api.views import profile
from user_role_api.views import user_role
from user_api.views import user_profile
from page_api.views import page_cl
from count_api.views import count_api

schema_view = get_schema_view(
   openapi.Info(
      title="Datahub",
      default_version='v1',
      description="Make migrations like brezes",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   
   path('register/', RegisterView.as_view(), name='register'),
   path('login/', LoginView.as_view(), name='login'),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('getconnection/',ListConnectionsAPIView.as_view(),name='ListConnectionsAPIView'),
   path('getconnection/<int:pk>/', ListConnectionsAPIView.as_view(), name='ListConnectionsAPIView'),
   path('postconnection/',CreateConnectionsAPIView.as_view(),name='CreateConnectionsAPIView'),
   path('putconnection/',UpdateConnectionsAPIView.as_view(),name='UpdateConnectionsAPIView'),
   path('putconnection/<int:pk>/', UpdateConnectionsAPIView.as_view(), name='UpdateConnectionsAPIView'),
   path('deleteconnection/<int:pk>/',DeleteConnectionsAPIView.as_view(),name='DeleteConnectionsAPIView'),
   path('schedule_dep/', schedule_dep.as_view()),
   path('schedule_dep/<int:pk>', schedule_dep.as_view()),
   path('sql_extract_api/', db_sql_extract.as_view()),
   path('sql_extract_api/<str:pk>', db_sql_extract.as_view()),
   path('pipe_sc/',pipeline_sch.as_view()),
   path('pipe_sc/<int:pk>',pipeline_sch.as_view()),
   path('pipeline/', pipe.as_view()),
   path('pipeline/<str:pk>', pipe.as_view()),
   path('pipeline_det/', Pipeline_detail.as_view()),
   path('pipeline_det/<str:pk>',Pipeline_detail.as_view()),
   path('connection_det/',detail.as_view()),
   path('connection_det/<int:pk>',detail.as_view()),
   path('db_config/',db_config_api.as_view()),
   path('db_config/<int:pk>',db_config_api.as_view()),
   path('role', role_name_api.as_view()),
   path('role/<int:pk>', role_name_api.as_view()),
   path('role_detail', role_details.as_view()),
   path('role_detail/<int:pk>', role_details.as_view()),
   path('profile/',profile.as_view()),
   path('user_role/',user_role.as_view()),
   path('user_api/',user_profile.as_view()),
   path('pages/',page_cl.as_view()),
   path('pages/<int:pk>',page_cl.as_view()),
   path('count/',count_api.as_view()),
   ]
