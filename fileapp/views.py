from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializer import FileSerializer
from rest_framework.generics import ListAPIView
from .models import FileData

# Create your views here.


class FileView(APIView):
    parser_classes = (MultiPartParser,FormParser)

    def post(self,request):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data,status=status.HTTP_201_CREATED)
        
        else:
            return Response(file_serializer.data, status=status.HTTP_400_BAD_REQUEST)


class FileAllView(ListAPIView):
    queryset = FileData.objects.all()
    serializer_class = FileSerializer