import math


def getPermutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """

    nums = [i for i in range(1, n + 1)]
    k -= 1
    res = []

    for j in range(n, 0, -1):
        factors = math.factorial(j - 1)
        index = k // factors
        res.append(str(nums.pop(index)))
        k %= factors

    return "".join(res)


print(getPermutation(3, 3))