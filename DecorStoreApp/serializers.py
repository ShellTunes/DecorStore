
from rest_framework import serializers, fields, filters
from rest_framework.serializers import ModelSerializer
from django.conf import settings
from .models import *
from django.contrib.auth import get_user_model



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"




class ProjectsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Projects
        fields = "__all__"