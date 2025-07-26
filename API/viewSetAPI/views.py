from django.shortcuts import render

# Create your views here.
from FunctionBasedAPI.models import Student
from FunctionBasedAPI.serializer import StudentSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class StudentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing API instances.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = [ 'age']  # ?student_class=Six
    search_fields = ['name']                     # ?search=rahim
    ordering_fields = ['name', 'age']            # ?ordering=age

    