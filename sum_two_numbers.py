def sum_two_numbers(a, b):
    """
    Add two numbers and return the result.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        The sum of a and b
    """
    return a + b


if __name__ == "__main__":
    # Example usage
    num1 = 5
    num2 = 10
    result = sum_two_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")

    # More examples
    print(f"Sum of 3.5 and 2.5: {sum_two_numbers(3.5, 2.5)}")
    print(f"Sum of -10 and 15: {sum_two_numbers(-10, 15)}")
