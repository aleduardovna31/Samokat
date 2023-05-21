import configuration
import requests

def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body)

def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         headers=track_number)