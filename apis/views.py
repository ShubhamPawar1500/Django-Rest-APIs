from django.shortcuts import render
from rest_framework import generics
from books.models import Book
from .serializers import BookSerializers, test
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .pagination import CustomePagination

# Create your views here.

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    pagination_class = CustomePagination

class BookDetailView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class CreateAPIView(APIView):
    def post(self, request, format=None):
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookUpdateView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    lookup_field = 'pk'

class BookDelete(generics.DestroyAPIView):
    serializer_class = BookSerializers
    lookup_url_kwarg = 'id'
    queryset = Book.objects.all()

