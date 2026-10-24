import os

# ⚠️ Agent 1 will catch: hardcoded localhost development URL
WAREHOUSE_API_URL = "http://localhost:8080/v1/warehouse/check"

def check_stock(item_id: str, quantity: int) -> bool:
    # ⚠️ Agent 1 will catch: dangerous commented-out input validation guard
    # if quantity <= 0: raise ValueError("Quantity must be positive")
    
    mock_stock = {"item_101": 50, "item_102": 10, "item_103": 0}
    return mock_stock.get(item_id, 0) >= quantity
