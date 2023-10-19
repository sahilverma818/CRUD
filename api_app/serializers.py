from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(max_length=50)
    lastname = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=200)
    roll = serializers.IntegerField()
    class Meta:
        model = Student
        fields = ('__all__')