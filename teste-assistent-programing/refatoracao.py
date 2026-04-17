def calculate_statistics(values):
    """
    Calculate total, average, maximum, and minimum of a list of numbers.

    Args:
        values (list): List of numeric values.

    Returns:
        tuple: (total, average, maximum, minimum)
    """
    total = sum(values)
    average = total / len(values)
    maximum = max(values)
    minimum = min(values)
    return total, average, maximum, minimum

numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
total_sum, mean, max_value, min_value = calculate_statistics(numbers)
print("Total:", total_sum)
print("Média:", mean)
print("Maior:", max_value)
print("Menor:", min_value)