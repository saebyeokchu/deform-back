from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from .service.post import Post
from .service.media import Media
from .service.order import Order
from .service.user import User
from .service.payment import Payment
from .service.product import Product


# Create your views here.
@api_view(['POST'])
def add_product(request) :
    if request.method == 'POST' :
        price = request.POST.get('price')
        try :
            Product.objects.create(price=price)
            return Response(status=status.HTTP_201_CREATED)
        except : 
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_post(request) :
    if request.method == 'POST' :
        try :
            responseText = Post.create(request.data)
            if responseText['link'] : 
                print('link : ', responseText['link'])
                return Response(responseText['link'],status=status.HTTP_201_CREATED)
        except :
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_post(request) :
    if request.method == 'GET' :
        #post = request.POST.get('post')
        try :
            Post.read()
            return Response(status=status.HTTP_201_CREATED)
        except :
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def add_media(request) :
    try :
        if(request.data.get('imgUrl')) :
            responseText = Media.upload(request.data)
            if responseText['id'] :
                return Response(responseText['id'], status=status.HTTP_201_CREATED)
    except :
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def make_order(request) :
    try :
        responseText = Order.make(request.data)
        return Response(responseText, status=status.HTTP_201_CREATED)
    except :
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# User Views
@api_view(['GET'])
def get_user(request) :
    try :
        responseText = User.get(request.GET.get('userId'))
        return Response(responseText, status=status.HTTP_201_CREATED)
    except :
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# Payment Views
@api_view(['GET'])
def get_all_payments(request) :
    try :
        responseText = Payment.getAllPayments()
        return Response(responseText, status=status.HTTP_201_CREATED)
    except :
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# Product View
@api_view(['POST'])
def create_product(request) :
    if request.method == 'POST' :
        try :
            responseText = Product.create(request.data)
            return Response(responseText,status=status.HTTP_201_CREATED)
        except :
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(['GET','POST'])
# def book_list(request) :
#     if request.method == 'GET' :
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST' :
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid() :
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET','PUT','DELETE'])
# def book_detail(request, pk):
#     try :
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET' :
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
#     elif request.method == 'PUT' :
#         serializer = BookSerializer(book, data = request.data)

        
        