def calculate_discount(price: float, discount_rate: float) -> float:
    print(f"DEBUG: calculating discount: price={price}, rate={discount_rate}")
    return price * (1.0 - discount_rate)

def calculate_average_discount(discounts: list) -> float:
    total = sum(discounts)
    return total / len(discounts)
