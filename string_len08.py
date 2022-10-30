def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    a = len(s)//2 -1
    b = len(s)//2
    if len(s)%2==1:
        return s[b]
    if len(s)%2==0:
        return s[b]+s[a]
print(main("abcdf"))
print(main("cool"))
