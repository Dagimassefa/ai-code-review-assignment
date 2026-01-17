# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
def average_valid_measurements(values):
    total_value = 0.0
    count = 0

    for value in values:
        if value is None:
            continue
        try:
            total_value += float(value)
            count += 1
        except (TypeError, ValueError):
            # Skip if the given value can not be converted to a float
            continue
    if count == 0:
        return 0.0
    return total_value / count
