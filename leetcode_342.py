def isPowerOfFour(n):
    """
    :type n: int
    :rtype: bool
    """
    def helper(n):
        if n == 1:
            return True
        if n % 4 != 0 or n == 0:
            return False
        return helper(n // 4)

    return helper(n)