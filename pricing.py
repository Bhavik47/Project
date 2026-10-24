def calculate_discount(price: float, discount_rate: float) -> float:
    # ⚠️ Agent 1 will catch: leftover debug print statement
    print(f"DEBUG: calculating discount: price={price}, rate={discount_rate}")
    return price * (1.0 - discount_rate)

def calculate_average_discount(discounts: list) -> float:
    # ⚠️ Agent 2 will catch & prove: ZeroDivisionError when discounts is empty []
    total = sum(discounts)
    return total / len(discounts)
