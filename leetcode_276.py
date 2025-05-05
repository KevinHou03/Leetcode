def numWays(n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """

    if n == 1:
        return k

    same = [0] * n # number of possibilities if n same as n - 1
    diff = [0] * n #number of possibilities if n not same as n - 1

    same[0], same[1] = 0, k
    diff[0], diff[1] = k, k * (k - 1)

    for i in range(2, n):
        same[i] = diff[i - 1]
        diff[i] = same[i - 1] * (k - 1) + diff[i - 1] * (k - 1)


    return same[-1] + diff[-1]


print(numWays(1,2))