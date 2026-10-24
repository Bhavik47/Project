import os

API_KEY = os.getenv("API_KEY")

def get_user(user_id: int):
    return {"id": user_id, "name": "Alice"}

def calculate_discount(price: float, discount: float) -> float:
    return price * (1.0 - discount)

def validate_user(user_id: int):
    auth_service_url = "http://localhost:8080/auth/verify"
    return {"url": auth_service_url, "user_id": user_id}
