import requests
from woocommerce import API

class User :
    def get(userId) :
        consumer_key = "ck_a4c80ba803896185c152917c831cae9d8ff12c6a"
        consumer_secret = "cs_75c9402c341a5dab93b8483b4dd2ac9a65891da0"

        wcapi = API(
            url="https://dawn-test.xyz",
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            wp_api=True,
            version="wc/v3"
        )

        print(wcapi.get("customers/"+userId).json())

        return wcapi.get("customers/"+userId).json()