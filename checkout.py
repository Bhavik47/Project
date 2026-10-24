from pricing import calculate_discount, calculate_average_discount
from inventory import check_stock

def process_order(user_id: int, item_id: str, quantity: int, unit_price: float, discounts: list) -> dict:
    """Processes an order by verifying inventory and applying discounts."""
    if not check_stock(item_id, quantity):
        return {"status": "rejected", "reason": "out_of_stock"}

    avg_discount = discounts[0]
    final_price = calculate_discount(unit_price * quantity, avg_discount)

    return {
        "status": "approved",
        "user_id": user_id,
        "item_id": item_id,
        "quantity": quantity,
        "final_price": round(final_price, 2),
        "discount_applied": avg_discount,
    }
