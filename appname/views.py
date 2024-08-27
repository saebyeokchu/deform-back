from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

# Create your views here.
@api_view(['GET','POST'])
def book_list(request) :
    if request.method == 'GET' :
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def book_detail(request, pk):
    try :
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET' :
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT' :
        serializer = BookSerializer(book, data = request.data)

        
        
