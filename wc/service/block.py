from ..models import blockboard
from ..serializers import blockboardSerializer

#Database Blockboard Service
class BlockService :

    def getAll(userId) :
        try : 
            serializer = blockboardSerializer(blockboard.objects.filter(userid = userId), many=True)
            print(serializer.data)
            return serializer.data
        except :
            return RuntimeError
        
    def get(userId, mediaId) :
        try : 
            item = blockboard.objects.filter(userid = userId)
                
            if mediaId :
                item = blockboard.objects.filter(mediaid = mediaId)

            serializer = blockboardSerializer(item, many=True)
            return serializer.data
        except :
            return RuntimeError

    def add(block : blockboard) :
        try :
            block.save()
            serializer = blockboardSerializer(block)
            return serializer.data
        except :
            return RuntimeError
        
    def update(userId, mediaId, shared, postId, productId) :
        try :
            print("userId,",userId,mediaId)
            item = blockboard.objects.get(
                userid = userId, 
                mediaid = mediaId
            )
            if item :
                print("item",item)
                item.shared = item.shared if shared is None else shared
                print("shared",shared)
                item.postid = item.postId if postId is None else postId
                print("postId",postId)
                item.productid = item.productid if productId is None else productid
                print("productid",productId)

                item.save()
                serializer = blockboardSerializer(item)
                return serializer.data
        except :
            return RuntimeError
        
    def delete(userId, mediaId) :
        try :
            item = blockboard.objects.get(
                userid = userId, 
                mediaid = mediaId
            )
            if item :
                item.delete()
            return True
        except :
            return RuntimeError
    
    def deleteByUserId(userId) :
        try :
            blockboard.objects.get(userid=userId).delete()
            return True
        except :
            return RuntimeError
        