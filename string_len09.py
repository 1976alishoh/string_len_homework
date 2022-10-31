def main(num1, num2):
    """
    Given two non-negative integers, num1 and num2 represented as string.
    Return the sum of num1 and num2 as a string.

    Args:
        num1: str
        num2: str
    Returns:
        str: answer
    """
    a = int(num1)
    b = int(num2)
    return  str(a + b)
print(main("12","5"))
print(main("425","81"))