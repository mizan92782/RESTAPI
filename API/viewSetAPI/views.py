from django.shortcuts import render

# Create your views here.
from FunctionBasedAPI.models import Student
from FunctionBasedAPI.serializer import StudentSerializer
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing API instances.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    