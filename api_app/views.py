from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Imports for rest framework 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Student
from.serializers import StudentSerializer
from api_app import serializers

# Create your views here.

class StudentView(APIView):
    
    def get(self,request):
        result = Student.objects.all()
        serializer = StudentSerializer(result, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

class StudentModify(APIView):

    def get(self, request, pk):
        try:
            result = Student.objects.get(pk = pk)
            print(result)
            if result:
                serializer = StudentSerializer(result)
                return Response(serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_204_NO_CONTENT, data="Error : Looks like data is missing at our end.")

    def post(self, request,pk):
        try:
            result = Student.objects.get(pk = pk)
            result.delete()
        except:
            pass
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    def delete(self, request, pk):
        try:
            result = Student.objects.get(pk = pk)
            result.delete()
        except:
            pass
        return Response(status=status.HTTP_200_OK, data="Data Deleted")
        
        