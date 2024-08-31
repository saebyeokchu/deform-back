from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import blockboard
from .serializers import blockboardSerializer
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
def update_post(request) :
    if request.method == 'POST' :
        try :
            responseText = Post.update(request.data)
            return Response(responseText,status=status.HTTP_202_ACCEPTED)
        except :
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['POST'])
def create_post(request) :
    if request.method == 'POST' :
        try :
            responseText = Post.create(request.data)
            return Response(responseText,status=status.HTTP_201_CREATED)
        except :
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_post(request) :
    if request.method == 'GET' :
        #post = request.POST.get('post')
        try :
            responseText = Post.read(request.GET.get["postId"])
            return Response(responseText, status=status.HTTP_201_CREATED)
        except :
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['get'])
def delete_media(request) :
    try :
        if(request.GET.get('mediaId')) :
            print(request.GET.get('mediaId'))
            responseText = Media.delete_media(request.GET.get('mediaId'))
            return Response(responseText, status=status.HTTP_200_OK)
    except :
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def add_media(request) :
    try :
        if(request.data.get('file')) :
            responseText = Media.upload(request.data)
            return Response(responseText, status=status.HTTP_201_CREATED)
    except :
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_media_by_author(request) :
    try :
        if(request.GET.get('userId')) :
            responseText = Media.getByAuthor(request.GET.get('userId'))
            return Response(responseText, status=status.HTTP_201_CREATED)
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

@api_view(['POST'])
def add_block(request) :
    try :
        block = blockboard(
            userid = request.data["userId"],
            mediaid = request.data["mediaId"],
            shared = True if request.data.get("shared") else False
        )
        block.save()
        item = blockboard.objects.filter(userid = request.data["userId"])
        serializer = blockboardSerializer(block)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except :
        return Response(status = status.HTTP_409_CONFLICT)

@api_view(['POST'])
def update_block(request) :
    try :
        print(request.data.get("userId"))

        item = blockboard.objects.get(userid = request.data.get("userId"), mediaid = request.data.get("mediaId"))
        item.shared = True if request.data.get("shared") else False
        item.save()

        serializer = blockboardSerializer(item)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    except :
        return Response(status = status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET'])
def get_block(request) :
    try :
        item = blockboard.objects.filter(userid = request.GET.get("userId"))
        
        if request.GET.get("mediaId") :
            item = blockboard.objects.filter(mediaid = request.GET.get("mediaId"))

        serializer = blockboardSerializer(item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except item.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
 

    # design = Design.objects.get(userid=request.GET.get("userId"))
    # print(design.query)
    # serializer = DesignSerializer(design)
    # return Response(serializer.data)
    # elif request.method == 'POST' :
    #     serializer = BookSerializer(data=request.data)
    #     if serializer.is_valid() :
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

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

        
        
