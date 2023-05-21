from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import StudentsFilter
from django.shortcuts import redirect
from rest_framework.response import Response

class StudentsFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsFilter
        fields = ('FilteringLevel', 'StudentSpecilized', 'StudentLevel', 'StudentClass')
