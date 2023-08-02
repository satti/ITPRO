from django.shortcuts import render
from . models import Subjects
from . serializers import SubjectsSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_subjects(request):
    #permission_classes = [IsAuthenticated] this is for class based views
    if request.method == 'GET':
        queryset = Subjects.objects.all()
        response = SubjectsSerializer(queryset,many=True)
        return Response(response.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_subject(request):
    permission_classes = [IsAuthenticated]
    if request.method == 'POST':
        data = request.data
        serializer = SubjectsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE','GET','PATCH'])
@permission_classes([IsAuthenticated])
def get_subject(request,pk):
    permission_classes = [IsAuthenticated]
    sub = Subjects.objects.get(id=pk)
    if request.method == 'GET':
        serializer = SubjectsSerializer(sub,many=False)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        sub.delete()
        return Response({'message': 'Subject Deleted...'})    
    elif request.method == 'PATCH':
        data = request.data
        serializer = SubjectsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
