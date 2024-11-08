# Мария Швецова, 23-я когорта — Финальный проект. Инженер по тестированию плюс
from data import order_body
from request import create_new_order, get_order_by_track

def test_order_creation_and_tracking():
    response_create = create_new_order(order_body)
    order_track = response_create.json().get("track")
    response_get = get_order_by_track(order_track)
    assert response_get.status_code == 200



