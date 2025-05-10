import math


class Solution(object):
    def isArmstrong(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = n
        k = len(str(n))
        _sum = 0
        start = k - 1
        while start >= 0:
            digit = n // math.pow(10, start)
            remainder = n % math.pow(10, start)
            _sum += math.pow(digit, k)
            start -= 1
            n = remainder

        return int(_sum) == a


