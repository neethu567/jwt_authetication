from .models import student
from rest_framework import serializers
from django.contrib.auth.models import User
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ('id', 'first_name', 'last_name')
