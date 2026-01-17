# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_average_order_value(orders):
    total_amount = 0.0
    order_count = 0

    for order in orders:
        # Skip if order is cancelled
        if order.get("status") == "cancelled":
            continue

        amount = order.get("amount")
        if amount is None:
            continue

        try:
            total_amount += float(amount)
            order_count += 1
        except (TypeError, ValueError):
            # skip if it is non-numeric value since we cant have an avarage of that
            continue

    if order_count == 0:
        return 0.0

    return total_amount / order_count
