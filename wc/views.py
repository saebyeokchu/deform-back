from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import auth, blockboard

from .serializers import blockboardSerializer
from .service.post import PostService
from .service.media import MediaService
from .service.order import OrderService
from .service.user import UserService
from .service.payment import PaymentService
from .service.product import ProductService
from .service.block import BlockService

# Create your views here.
class BlockView : 

    @api_view(['GET'])
    def getAll(request) :
        try :
            userId = request.GET.get("userId")
            if userId :
                return_data = BlockService.getAll(userId)
                return Response(return_data, status=status.HTTP_200_OK)
            else :
                return Response(status=status.HTTP_404_NOT_FOUND)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    @api_view(['GET'])
    def get(request) :
        try :
            userId = request.GET.get("userId")
            mediaId = request.GET.get("mediaId")
            if userId :
                return_data = BlockService.get(userId, mediaId)
                return Response(return_data, status=status.HTTP_200_OK)
            else :
                return Response(status=status.HTTP_404_NOT_FOUND)
        except :
            return Response(status = status.HTTP_404_NOT_FOUND)
        
    @api_view(['POST'])
    def add(request) :
        try :
            block = blockboard(
                userid = request.data["userId"],
                mediaid = request.data["mediaId"],
                shared = True if request.data.get("shared") else False
            )
            return_data = BlockService.add(block)
            return Response(return_data, status=status.HTTP_201_CREATED)
        except :
            return Response(status = status.HTTP_409_CONFLICT)

    @api_view(['POST'])
    def update(request) :
        try :
            userId = request.data.get("userId")
            mediaId = request.data.get("mediaId")
            shared = request.data.get("shared")
            postId = request.data.get("postId")

            if userId and mediaId :
                return_data = BlockService.update(userId, mediaId, shared, postId)
                return Response(return_data, status=status.HTTP_202_ACCEPTED)
            else :
                return Response(status=status.HTTP_404_NOT_FOUND)
        except :
            return Response(status = status.HTTP_406_NOT_ACCEPTABLE)
        

    @api_view(['GET'])
    def delete(request) :
        try :
            userId = request.GET.get("userId")
            mediaId = request.GET.get("mediaId")

            if mediaId and userId :
                BlockService.delete(userId, mediaId)
                return Response(status=status.HTTP_200_OK)
            else :
                return Response(status=status.HTTP_404_NOT_FOUND)
        except :
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['GET'])
    def deleteByUserId(request) :
        try :
            userId = request.GET.get("userId")
            if userId :
                BlockService.deleteByUserId(userId)
                return Response(status=status.HTTP_200_OK)
            else :
                return Response(status=status.HTTP_404_NOT_FOUND)
        except :
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ProductView :
    @api_view(['POST'])
    def create(request) :
        if request.method == 'POST' :
            try :
                responseText = ProductService.create(request.data)
                return Response(responseText,status=status.HTTP_201_CREATED)
            except :
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
    @api_view(['POST'])
    def add(request) :
        if request.method == 'POST' :
            price = request.POST.get('price')
            try :
                ProductService.objects.create(price=price)
                return Response(status=status.HTTP_201_CREATED)
            except : 
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PostView :
    @api_view(['POST'])
    def update(request) :
        if request.method == 'POST' :
            try :
                print(request.data)
                responseText = PostService.update(request.data)
                return Response(responseText,status=status.HTTP_202_ACCEPTED)
            except :
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    @api_view(['POST'])
    def create(request) :
        if request.method == 'POST' :
            try :
                responseText = PostService.create(request.data)
                return Response(responseText,status=status.HTTP_201_CREATED)
            except :
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @api_view(['GET'])
    def get(request) :
        if request.method == 'GET' :
            #post = request.POST.get('post')
            try :
                responseText = PostService.read(request.GET.get["postId"])
                return Response(responseText, status=status.HTTP_201_CREATED)
            except :
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    @api_view(['GET'])
    def delete(request) :
        if request.method == 'GET' :
            #post = request.POST.get('post')
            try :
                responseText = PostService.delete(request.GET.get("postId"))
                return Response(responseText, status=status.HTTP_200_OK)
            except :
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class MediaView : 
    @api_view(['GET'])
    def get_media_by_author(request) :
        try :
            if(request.GET.get('userId')) :
                responseText = MediaService.getByAuthor(request.GET.get('userId'))
                return Response(responseText, status=status.HTTP_201_CREATED)
            else :
                return Response(status=status.HTTP_404_NOT_FOUND)
        except :
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['POST'])
    def add(request) :
        try :
            print(request.data.get('file'))
            if(request.data.get('file')) :
                responseText = MediaService.upload(request.data)
                print(responseText)
                return Response(responseText, status=status.HTTP_201_CREATED)
            else :
                return Response(status=status.HTTP_404_NOT_FOUND)
        except :
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['get'])
    def delete(request) :
        try :
            if(request.GET.get('mediaId')) :
                print(request.GET.get('mediaId'))
                responseText = MediaService.delete_media(request.GET.get('mediaId'))
                return Response(responseText, status=status.HTTP_200_OK)
            else :
                return Response(status=status.HTTP_404_NOT_FOUND)
        except :
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class OrderView : 
    @api_view(['POST'])
    def make_order(request) :
        try :
            responseText = OrderService.make(request.data)
            return Response(responseText, status=status.HTTP_201_CREATED)
        except :
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserView :
    # User Views
    @api_view(['GET'])
    def get_user(request) :
        try :
            print(request)
            responseText = UserService.get(request.GET.get('userId'))
            return Response(responseText, status=status.HTTP_201_CREATED)
        except :
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['GET'])
    def get_auth(request) :
        try :
            userId = request.GET.get("userId")
            if userId :
                return_data = UserService.get_auth(userId)
                return Response(return_data, status=status.HTTP_200_OK)
            else :
                 return Response(status = status.HTTP_404_NOT_FOUND) 
        except :
            return Response(status = status.HTTP_404_NOT_FOUND)
    
    @api_view(['POST'])
    def update_auth(request) :
        try :
            token = request.data.get("token")

            if token :
                return_data = UserService.update_auth(token)
                return Response(return_data, status=status.HTTP_202_ACCEPTED)
            else :
                return Response(status = status.HTTP_409_CONFLICT)
            
        except :
            return Response(status = status.HTTP_406_NOT_ACCEPTABLE)
        
    @api_view(['POST'])
    def add_auth(request):
        try :
            auth_input = auth(
                userid = request.data["userId"],
                token = request.data["token"]
            )
            print(auth_input)
            return_data = UserService.add_auth(auth_input)
            return Response(return_data, status=status.HTTP_201_CREATED)
        except :
            return Response(status = status.HTTP_409_CONFLICT)
    
    @api_view(['get'])
    def delete_auth(request) :
        try :
            userId = request.GET.get("userId")

            if userId :
                UserService.delete_auth(userId)
                return Response(status=status.HTTP_200_OK)
            else :
                return Response(status=status.HTTP_404_NOT_FOUND)
        except :
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete_auth_all(request) :
        try :
            userId = request.GET.get("userId")

            if userId :
                UserService.delete_auth_all(userId)
                return Response(status=status.HTTP_200_OK)
            else :
                return Response(status=status.HTTP_404_NOT_FOUND)
        except :
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PaymentView :
    # Payment Views
    @api_view(['GET'])
    def get_all_payments(request) :
        try :
            responseText = PaymentService.getAllPayments()
            return Response(responseText, status=status.HTTP_201_CREATED)
        except :
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


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

        
        
