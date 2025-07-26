from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializer import StudentSerializer

from .models import Student

@api_view(['GET'])
@permission_classes([AllowAny])
def getApi(request):
  students= Student.objects.all()
  serializer = StudentSerializer(students, many=True)
  
  return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def postApi(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)



@api_view(['PATCH'])
def updateApi(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)
    
    serializer = StudentSerializer(student, data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)



@api_view(['DELETE'])
def deleteApi(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)
    
    student.delete()
    return Response(status=204)




# List & Create
@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, Update, Delete by ID
@api_view(['GET', 'POST','PUT', 'DELETE'])
def allApi(request, pk=None):
    if pk is None:
      if request.method == 'GET':
          students = Student.objects.all()
          serializer = StudentSerializer(students, many=True)
          return Response(serializer.data)
    else:
      try:
          student = Student.objects.get(pk=pk)
      except Student.DoesNotExist:
          return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
      
      if request.method == 'GET':
          serializer = StudentSerializer(student)
          return Response(serializer.data)
      
      elif request.method == 'PUT':
          serializer = StudentSerializer(student, data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      elif request.method == 'DELETE':
          student.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
