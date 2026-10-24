import os

WAREHOUSE_API_URL = "http://localhost:8080/v1/warehouse/check"

def check_stock(item_id: str, quantity: int) -> bool:
    mock_stock = {"item_101": 50, "item_102": 10, "item_103": 0}
    return mock_stock.get(item_id, 0) >= quantity
