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
    if a and b and c :
        return s1,s2,s3
    if a and b   :
        return s1,s2,
    if a   :
        return s1
    
    if a and c :
        return s1,s3,
    if c  :
        return s3
    
    if b and c :
        return s2,s3,
    if b  :
        return s2
    
    else:
        return "[]"
print(main("code", "python","coder"))
print(main("codeschool.uz","example","python"))