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
    if len(s)%2==1 :
        return str(s[b])
    if len(s)%2==0 :
        return str(s[b]+s[a])
    if len(s)==2:
        return s[::-1]
print(main("abcdf"))
print(main("cool"))
