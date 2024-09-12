from .api import sendWoocommerceAPI

class ProductService : 
    def create(productData):
        wcapi = sendWoocommerceAPI()
        return wcapi.post("products", productData).json()

