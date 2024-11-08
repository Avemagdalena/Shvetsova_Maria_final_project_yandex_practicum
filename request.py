import configuration
import requests
import data

def create_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body,
                         headers=data.header)

def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(track))

