def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    a=len(s1)%2==1
    b=len(s2)%2==1
    c=len(s3)%2==1
    l = []
    if a:
        l.append(s1)
    if b:
        l.append(s2)
    if c:
        l.append(s3)
    return l
print(main("code","coder","python"))    