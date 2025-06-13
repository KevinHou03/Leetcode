def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    if n == 1:
        return True
    def aux(k):
        if k == n:
            return True
        elif k > n:
            return False
        else:
            return aux(k * 2)

    return aux(1)


n = 18
print(isPowerOfTwo(n))

