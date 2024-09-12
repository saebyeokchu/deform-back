from .api import sendWoocommerceAPI

class PaymentService :
    def getAllPayments() :
        wcapi = sendWoocommerceAPI()
        return wcapi.get("payment_gateways").json()