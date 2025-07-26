from django.shortcuts import render

# Create your views here.
#! # Create a mixin for handling student data ap8i
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from FunctionBasedAPI.models import Student
from FunctionBasedAPI.serializer import StudentSerializer

class StudentMixin(GenericAPIView, 
                   ListModelMixin, 
                   CreateModelMixin, 
                   UpdateModelMixin, 
                
                   DestroyModelMixin, 
                   RetrieveModelMixin):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)  # For retrieving a single object
        return self.list(request, *args, **kwargs)          # For listing all objects

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)        # Full update

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)  # Partial update

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

