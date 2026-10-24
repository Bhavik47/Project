import os

API_KEY = os.getenv("API_KEY")

def get_user(user_id: int):
    return {"id": user_id, "name": "Alice"}

def calculate_discount(price: float, discount: float) -> float:
    print(f"DEBUG: calculating discount for price={price}, discount={discount}")
    return price * (1.0 - discount)

