def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    def helper(n):
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        return helper(n // 3)

    return helper(n)