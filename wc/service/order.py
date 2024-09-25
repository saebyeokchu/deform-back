import json
from .api import sendWoocommerceAPI

class OrderService : 
    def make(orderData):
        wcapi = sendWoocommerceAPI()
        return wcapi.post("orders", orderData).json()

