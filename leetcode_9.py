def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    s_x = str(x)
    for i in range(len(s_x)):
        if s_x[i] != s_x[len(s_x)-(i+1)]:
            return False
    return True

x = 12321
print(isPalindrome(x))



