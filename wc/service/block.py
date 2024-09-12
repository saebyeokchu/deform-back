from ..models import blockboard
from ..serializers import blockboardSerializer

#Database Blockboard Service
class BlockService :
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
        
    def update(userId, mediaId, shared) :
        try :
            item = blockboard.objects.get(
                userid = userId, 
                mediaid = mediaId
            )
            item.shared = True if shared else False
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
        